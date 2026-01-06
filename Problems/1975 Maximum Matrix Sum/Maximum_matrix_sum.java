class Solution {
    public long maxMatrixSum(int[][] matrix) {
        long sum_of_matrix = 0;
        int number_of_negatives = 0;
        int smallest_abs = 9999999;

        for (int row = 0; row < matrix.length; row ++){
            for (int col = 0; col < matrix[row].length; col ++){
                int element = matrix[row][col];
                sum_of_matrix += Math.abs(element);
                if (Math.abs(element) < smallest_abs){
                    smallest_abs = Math.abs(element);
                }
                if (element <= 0){
                    number_of_negatives ++;
                }
            }
        }
        if (number_of_negatives % 2 == 1){
            return sum_of_matrix - (2 * smallest_abs);
        }
        return sum_of_matrix;
    }
}