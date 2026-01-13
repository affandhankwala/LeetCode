class Solution {
    public int minTimeToVisitAllPoints(int[][] points) {
        int min_time = 0;
        if (points.length < 2){
            return min_time;
        }
        int i = 0, j = 1;
        while (j < points.length){
            int[] p1 = points[i], p2 = points[j];
            int[] difference = {Math.abs(p2[0] - p1[0]), Math.abs(p2[1] - p1[1])};
            int min_elem = difference[0];
            if (difference[1] < difference[0]){
                min_elem = difference[1];
            }
            min_time += min_elem;
            for (int d : difference) { 
                d -= min_elem;
                min_time += d;
            }
            i++;
            j++;            
        }
        return min_time;
    }
}