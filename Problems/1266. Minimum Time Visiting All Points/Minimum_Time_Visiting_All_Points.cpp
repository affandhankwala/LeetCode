class Solution {
public:
    int minTimeToVisitAllPoints(vector<vector<int>>& points) {
        int min_time = 0;
        if (points.size() < 2){
            return min_time;
        }
        int i = 0, j = 1;
        while (j < points.size()){
            vector<int> p1 = points[i], p2 = points[j];
            vector<int> difference(2);
            difference[0] = abs(p2[0] - p1[0]);
            difference[1] = abs(p2[1] - p1[1]);
            int smallest_diff_coor = *min_element(difference.begin(), difference.end());
            min_time += smallest_diff_coor;
            difference[0] -= smallest_diff_coor;
            difference[1] -= smallest_diff_coor;
            min_time += difference[0];
            min_time += difference[1];
            i++;
            j++;
        }
        return min_time;
    }
};