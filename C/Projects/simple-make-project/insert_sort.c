void insertionSort(int A[], int n) {
	int i,key;
	for (int j=1; j <= n-1; j++) {
		key = A[j];
		i = j - 1;
		while (i >= 0 && A[i] > key) {
			A[i+1] = A[i];
			i--;
		}
		A[i+1] = key;
	}
}
