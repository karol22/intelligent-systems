#Import required packages
import math
from pomegranate import *

# Initially the exam_level
exam_level =DiscreteDistribution( { 'd': 0.7, 'e': 0.3} )

# Initially the exam_level
iq_level =DiscreteDistribution( { 'l': 0.8, 'h': 0.2} )

# marks depends on exam_level and iq_level
marks =ConditionalProbabilityTable(
[[ 'd', 'l', 'l', 0.6 ],
[ 'd', 'l', 'h', 0.4 ],
[ 'd', 'h', 'l', 0.9 ],
[ 'd', 'h', 'h', 0.1 ],
[ 'e', 'l', 'l', 0.5 ],
[ 'e', 'l', 'h', 0.5 ],
[ 'e', 'h', 'l', 0.8 ],
[ 'e', 'h', 'h', 0.2 ]], [exam_level, iq_level] )

# apt_score depends on iq_level
apt_score =ConditionalProbabilityTable(
[['l', 'l', 0.75 ],
['l', 'h', 0.25 ],
['h', 'l', 0.4 ],
['h', 'h', 0.6 ],
], [iq_level] )

# admission depends on marks
admission =ConditionalProbabilityTable(
[['l', 'a', 0.6 ],
['l', 'r', 0.4 ],
['h', 'a', 0.9 ],
['h', 'r', 0.1 ],
], [marks] )

d1 = State( exam_level, name="exam_level" )
d2 = State( iq_level, name="iq_level" )
d3 = State( marks, name="marks" )
d4 = State( apt_score, name="apt_score" )
d5 = State( admission, name="admission" )
 
#Building the Bayesian Network
network = BayesianNetwork( "Admission to University Problem With Bayesian Networks" )
network.add_states(d1, d2, d3, d4, d5)
network.add_edge(d1, d3)
network.add_edge(d2, d3)
network.add_edge(d2, d4)
network.add_edge(d3, d5)
network.bake()


suma = 0
acceptediflowapt = 0
print("These are all the Joint Probabilities for all the 5 events: \n")
for ex in ['d', 'e']:
    for iq in ['l', 'h']:
        for mrk in ['l', 'h']:
            for apt in ['l', 'h']:
                for ad in ['a', 'r']:
                    (print("P(Exam: {} IQ: {} Apt: {} Marks: {} Admission: {}) = {:.5f}"
                    .format(ex, iq, apt, mrk, ad, network.probability([[ex, iq, apt, mrk, ad]]))))
                    if(ad == 'a'):
                        suma+= network.probability([[ex, iq, apt, mrk, ad]])
                    if(ad == 'a' and apt == 'l'):
                        acceptediflowapt+= network.probability([[ex, iq, apt, mrk, ad]])

print("Sum of probabilities: ", suma)
print("P(Accepted if low apt. score): ", acceptediflowapt)


"""print(network.probability([['e', 'h', 'h']]))
print(network.predict_proba({}))
print(suma)
print(network.predict_proba([[None, None, None, None, 'r']]))
"""

# Prob of high iq given accepted
print(network.predict_proba({'admission': 'r'}))

# Prob of being accepted
print(network.predict_proba({}))

# Prob of being accepted given low aptitude
#print(network.predict_proba({}))
#print(network.predict_proba({'apt_score': 'l'}))

# 