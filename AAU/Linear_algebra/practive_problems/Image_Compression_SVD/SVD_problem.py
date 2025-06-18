import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load image into a matrix

def load_image(image_path):
    img = Image.open(image_path).convert("L")  # Load image and convert to grayscale
    img_matrix = np.array(img, dtype=np.uint8)  # Convert image to numpy array
    return img_matrix

def perform_SVD(A: np.array) -> tuple:
    # Trin 1: Beregn A^T A og A A^T
    ATA = np.dot(A.T, A)
    AAT = np.dot(A, A.T)
    
    # Trin 2: Find egenværdier og egenvektorer for A^T A (til V)
    eigenvalues_ATA, V = np.linalg.eigh(ATA)  # eigh for symmetrisk matrix
    idx = np.argsort(eigenvalues_ATA)[::-1]  # Sorter faldende
    eigenvalues_ATA = eigenvalues_ATA[idx]
    V = V[:, idx]
    V_T = V.T
    # Trin 3: Find egenværdier og egenvektorer for A A^T (til U)
    eigenvalues_AAT, U = np.linalg.eigh(AAT)
    idx = np.argsort(eigenvalues_AAT)[::-1]
    eigenvalues_AAT = eigenvalues_AAT[idx]
    U = U[:, idx]
    
    # Trin 4: Konstruér Sigma
    m, n = A.shape
    singular_values = np.sqrt(np.maximum(eigenvalues_ATA, 0))  # Undgå negative værdier
    Sigma = np.zeros((m, n))
    np.fill_diagonal(Sigma, singular_values)

    
    return U, Sigma, V_T

def perform_compression(U, Sigma, V_T, k=None):
    A_compressed = None
    if k is not None:
        if k < 1 or k > min(m, n):
            raise ValueError(f"k skal være mellem 1 og {min(m, n)}.")
        U_k = U[:, :k]
        Sigma_k = Sigma[:k, :k]
        V_k_T = V_T[:k, :]
        A_compressed = np.dot(np.dot(U_k, Sigma_k), V_k_T)
    return A_compressed
    
def visualize_images(original, compressed, k):
    """Visualiserer originale og komprimerede billeder."""
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.imshow(original, cmap='gray')
    plt.title('Originalt billede')
    plt.axis('off')
    
    if compressed is not None:
        plt.subplot(1, 2, 2)
        plt.imshow(compressed, cmap='gray')
        plt.title(f'Komprimeret billede (k={k})')
        plt.axis('off')
    
    plt.tight_layout()
    plt.show()



    
image_matrix = load_image("boat.png")
U, Sigma, V_T = perform_SVD(image_matrix)
perform_compression(U, Si)
visualize_images(image_matrix, A_reconstructed, 10)
# Perform SVD on the image matrix


