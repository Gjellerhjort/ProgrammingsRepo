function [solution, value] = optimizeRoutes(C, P, D)
% optimizeRoutes solves the linear programming problem for network routing
% This function finds the optimal solution for routing given demands through
% a network as specified in the Workshop.
%
% Inputs are
%   C: Matrix where capacity of arc (i,j) is C(i,j)
%   P: Matrix where price of arc (i,j) is P(i,j)
%   D: Matrix where the demand from i to j is D(i,j)
%
% Outputs are
%   solution: The values of the variables in the solution as a vector. The
%             variables are ordered according to the demand matrix (in row-
%             wise fashion), and then according to arc ordering in C.
%   value: The value of the problem.
    if size(C,1)~=size(C,2) || size(P,1)~=size(P,2) || size(D,1)~=size(D,2) ...
                  || size(C,1)~=size(P,1) || size(C,1)~=size(D,1) || size(P,1)~=size(D,1)
        error("Matrices C, P, and D must be square and of same dimensions!")
    end
    
    nRoutes = nnz(D);

    % Form the objective function by concatenating the rows of P as many times
    % as there are routes in the demand matrix
    f = repmat(reshape(P', numel(P), 1), nRoutes, 1);

    % Add the edge capacity constraints to the matrix A and vector b
    % each row has the form [e_i,e_i,...,e_i]<=c_i where c_i is the i'th element
    % in C when traversed row-wise
    A = repmat(eye(numel(C)), nRoutes);
    b = repmat(reshape(C', numel(C), 1), nRoutes,1);

    % Construct a matrix containing the conditions on preservation of data trough
    % each vertex. For a specific demand (s,t) the submatrix has the form
    % [0111|1000|1000|1000]=0
    % [0100|1011|0100|0100]=0
    % [0010|0010|1101|0010]=0
    % [0001|0001|0001|1110]=0
    % (except when considering the source or destination for a demand. Then the
    % right-hand side must be +/- the demand).
    % These are then put in a diagonal block matrix with a diagonal matrix for
    % each (s,t) (this is why the Kronecker product is used)
    APreserve = kron(...
        eye(size(C)),ones(1,size(C,2))) - ...
        repmat(eye(size(C)), 1, size(C,1));
    APreserve = kron(eye(nRoutes), APreserve);

    % Initialize the right-hand side
    % (demands and zeros will be filled into appropriate entries in later loop)
    bPreserve = zeros(0);


    % Construct the matrix ensuring that demands are met
    ADemand = zeros(0);
    bDemand = zeros(0);
    % Loop over all entries in D to find the nonzero demands
    for i = 1:size(D,1)
        for j = 1:size(D,2)
            if D(i,j)==0
                continue
            end
            % Fill in demand in bPreserve
            bPreserve = [bPreserve; D(i,j)*(cbv(size(C,2),i)-cbv(size(C,2),j))'];
            
            allOnes = ones(1, size(C,2));
            % Demand is met for source if we include row
            % [0000|1111|0000|0000]=d
            % where the ones are in the position corresponding to the vertex number
            tmpMat = kron(cbv(size(C,2),i), allOnes);
            
            % Demand is met for destination if we include row
            % [0010|0010|0010|0010]=d
            % where the ones are in the position corresponding to the vertex number
            tmpMat = [tmpMat; kron(allOnes, cbv(size(C,2),j))];
            
            ADemand = blkdiag(ADemand,tmpMat);
            bDemand = [bDemand; D(i,j); D(i,j)];
        end
    end

    % Define lower bound to ensure that all variables are positive
    lb = zeros(length(f),1);

    [solution, value] = linprog(f, A, b, [APreserve; ADemand], [bPreserve; bDemand], lb);
    
    if length(solution)==0
        % No solution was found
        return
    end

    if isInteger(value)
        fprintf("Problem value is %d.\n\n",value);
    else
        fprintf("Problem value is %f.\n\n",value);
    end

    % Present solution in matrix form
    count = 0;
    for i = 1:size(D,1)
        for j = 1:size(D,2)
            if D(i,j)==0
                continue
            end
            fprintf("Routing %.2f from vertex %d to vertex %d via arcs:\n", D(i,j), i, j);
            entries = solution((1+count*numel(C)):(count+1)*numel(C), 1);
            disp(reshape(entries, size(C))');
            count = count + 1;
        end
    end
end


%% Helper function to return the i'th canonical basis vector of R^n
function v = cbv(n,i)
    tmp = eye(n);
    v = tmp(i,:);
end

function b = isInteger(n)
    b = mod(n,1)==0;
end