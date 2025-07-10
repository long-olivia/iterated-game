import os
import sys
import json

# {
#     "round": 1,
#     "a_contribution": 10,
#     "a_reasoning": "By contributing the maximum 10 points in the first round, I demonstrate trust and commitment towards maximizing the overall pool. This approach encourages cooperation from the other agent, increasing the total resources we all receive.",
#     "a_gain": 13.600000000000001,
#     "a_total_points_after_round": 13.600000000000001,
#     "b_contribution": 7,
#     "b_reasoning": "This is a classic public goods game with a multiplier of 1.6. Since there are 2 players, if both players contribute all 10 points, the total pool would be 20 points, multiplied by 1.6 = 32 points, giving each player 16 points back. This is better than keeping all 10 points individually. However, there's a free-rider problem where I could benefit more by contributing 0 while the other player contributes 10. But if we both think this way, we both get worse outcomes. Since this is the first round and I want to establish cooperative behavior and signal trustworthiness, I'll contribute a substantial amount but not everything, leaving room to adjust based on the other player's behavior.",
#     "b_gain": 16.6,
#     "b_total_points_after_round": 16.6,
#     "total_contribution_round": 17
# },

#final average dictionary. the key is the prompt pair, and the value is the array
basic_final_avg={}
discrim_final_avg={}
#round average dictionary. the key is the prompt pair, and the value is an array of averages
basic_round_avg={}
discrim_round_avg={}

"""
The final_average function takes a path string. It goes into the specified directory, sums up
total_points_after_round for each model's 20th round, and averages those points. It returns an array with these two averages.
"""

def final_average(path):
    a_sum=0
    b_sum=0
    average=[]
    return average

"""
The per_round_avg function takes a path string. It goes into the specified directory, and for each round, it 
sums up the contribution for each model. When the sums are done, everything is averaged.
"""

def per_round_avg(path):
    a_round_avg=[0]*20
    b_round_avg=[0]*20
    for i in range(0,20):
        __doc__
"""
The run function takes a directory (basic_results or discrim_results) and runs final_average & per_round_avg for each prompt pair.
It adds the return value of each function to the global dictionaries defined above. After it's done, it dumps the global dictionaries
into a json file within the upper level directory.
"""

def run(directory_name):
    prompt_pairs=["CC", "CN", "CS", "NC", "NN", "NS", "SC", "SN", "SS"]
    for name in prompt_pairs:
        path=f"{directory_name}/{name}"
        if (directory_name == "basic_results"):
            basic_final_avg[name] = final_average(path)
            basic_round_avg[name] = per_round_avg(path)
        else:
            discrim_final_avg[name] = final_average(path)
            discrim_round_avg[name] = per_round_avg(path)

if __name__ == "__main__":
    base_dir="/"
    run("basic_results")
    with open('basic_final.json', 'w') as b:
        json.dump(basic_final_avg, b)
    with open('basic_round.json', 'w') as b1:
        json.dump(basic_round_avg, b1)
    run("discrim_results")
    with open('discrim_final.json', 'w') as d:
        json.dump(discrim_final_avg, d)
    with open('discrim_round.json', 'w') as d1:
        json.dump(discrim_round_avg, d1)