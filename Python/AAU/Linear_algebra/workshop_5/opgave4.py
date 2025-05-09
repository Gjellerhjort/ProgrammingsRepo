import numpy as np
from scipy.optimize import linprog

# Matrix C
C = np.array([
    [0, 0, 25, 0, 0, 0, 0, 0],
    [5, 0, 0, 8, 0, 0, 0, 0],
    [0, 0, 0, 20, 0, 10, 0, 0],
    [0, 8, 20, 0, 10, 15, 0, 12],
    [0, 0, 15, 0, 0, 12, 0, 0],
    [0, 0, 0, 0, 12, 0, 8, 0],
    [5, 0, 0, 0, 15, 0, 0, 0],
    [0, 0, 0, 12, 0, 8, 15, 0]
])

# Matrix P
P = np.array([
    [0, 0, 6, 0, 0, 0, 0, 0],
    [3, 0, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 8, 0, 0],
    [0, 3, 6, 0, 10, 6, 0, 10],
    [0, 0, 5, 0, 0, 8, 0, 0],
    [0, 0, 0, 0, 8, 0, 4, 0],
    [3, 0, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 10, 0, 4, 5, 0]
])

# Matrix D
D = np.array([
    [0, 0, 0, 0, 0, 20, 0, 0],
    [0, 0, 0, 0, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 0, 0, 0, 0, 0]
])

def cbv(n, i):
    """Return the i-th canonical basis vector of R^n (1-based indexing)."""
    v = np.zeros(n)
    v[i - 1] = 1
    return v

def optimizeRoutes(C, P, D):
    # Check if matrices are square and of the same size
    if (C.shape[0] != C.shape[1] or P.shape[0] != P.shape[1] or D.shape[0] != D.shape[1] or
        C.shape[0] != P.shape[0] or C.shape[0] != D.shape[0] or P.shape[0] != D.shape[0]):
        raise ValueError("Matrices C, P, and D must be square and of same dimensions!")

    n = C.shape[0]  # Number of nodes
    nRoutes = np.count_nonzero(D)  # Number of non-zero demands

    # Objective function: Concatenate P flattened (row-wise) nRoutes times
    f = np.tile(P.T.flatten(), nRoutes)  # Shape: (nRoutes * n * n,)

    # Capacity constraints: sum(x[i,j,s,t]) <= C[i,j] for each arc (i,j)
    A = np.zeros((n * n, n * n * nRoutes))  # Shape: (n * n, n * n * nRoutes)
    for k in range(nRoutes):
        start_idx = k * n * n
        for i in range(n):
            for j in range(n):
                arc_idx = i * n + j
                A[arc_idx, start_idx + arc_idx] = 1
    b = C.T.flatten()  # Shape: (n * n,)

    # Flow preservation constraints
    APreserve_single = np.kron(np.eye(n), np.ones((1, n))) - np.tile(np.eye(n), (1, n))
    APreserve = np.kron(np.eye(nRoutes), APreserve_single)  # Block diagonal
    bPreserve = []

    # Demand constraints
    ADemand = []
    bDemand = []

    # Loop over D to find non-zero demands
    count = 0
    for i in range(n):
        for j in range(n):
            if D[i, j] == 0:
                continue
            # Flow preservation RHS: +D(s,t) at source, -D(s,t) at sink, 0 elsewhere
            bPreserve.extend(D[i, j] * (cbv(n, i + 1) - cbv(n, j + 1)))

            # Demand constraints: Outgoing from source = D(s,t), Incoming to sink = D(s,t)
            all_ones = np.ones(n)
            tmpMat = np.kron(cbv(n, i + 1), all_ones)  # Outgoing from source
            tmpMat = np.vstack([tmpMat, np.kron(all_ones, cbv(n, j + 1))])  # Incoming to sink
            # Pad tmpMat with zeros for other demands
            tmpMat_padded = np.zeros((tmpMat.shape[0], n * n * nRoutes))
            start_idx = count * n * n
            tmpMat_padded[:, start_idx:start_idx + n * n] = tmpMat
            if count == 0:
                ADemand = tmpMat_padded
            else:
                ADemand = np.vstack([ADemand, tmpMat_padded])
            bDemand.extend([D[i, j], D[i, j]])
            count += 1

    bPreserve = np.array(bPreserve)
    bDemand = np.array(bDemand)

    # Combine equality constraints
    A_eq = np.vstack([APreserve, ADemand])
    b_eq = np.concatenate([bPreserve, bDemand])

    # Bounds: All variables >= 0
    lb = [(0, None)] * len(f)

    # Solve the linear programming problem
    result = linprog(f, A_ub=A, b_ub=b, A_eq=A_eq, b_eq=b_eq, bounds=lb, method='highs')

    if not result.success:
        print("Optimization failed:", result.message)
        return None, None

    solution = result.x
    value = result.fun

    # Output results
    if value.is_integer():
        print(f"Problem value is {int(value)}.\n")
    else:
        print(f"Problem value is {value:.6f}.\n")

    # Present solution in matrix form
    count = 0
    for i in range(n):
        for j in range(n):
            if D[i, j] == 0:
                continue
            print(f"Routing {D[i, j]:.2f} from vertex {i + 1} to vertex {j + 1} via arcs:")
            entries = solution[count * n * n:(count + 1) * n * n]
            print(entries.reshape(n, n).T, "\n")
            count += 1

    return solution, value

# Run the optimization
solution, value = optimizeRoutes(C, P, D)
print("Solution:", solution)
print("Value:", value)