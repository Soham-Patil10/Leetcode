class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        min_time = float('inf')
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                #land 1st then water
                land_finish=landStartTime[i]+landDuration[i]
                water_start=max(land_finish,waterStartTime[j])
                total1=water_start+waterDuration[j]
                #water 1st then land
                water_finish=waterStartTime[j]+waterDuration[j]
                land_start=max(water_finish,landStartTime[i])
                total2=land_start+landDuration[i]
                current_best=min(total1,total2)
                if current_best<min_time:
                    min_time = current_best
        return min_time