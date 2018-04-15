#!/usr/bin/env python3
"""Simulation of M/M/1 queue"""

import heapq
import random


la = 3
mu = 5
rho = la / mu


def exp_service():
#    return np.random.exponential(1.0 / mu)
    return random.expovariate(mu)

def exp_arrival():
#    return np.random.exponential(1.0 / la)
    return random.expovariate(la)


timeline = []
queue = []

first_event = (0, "arrival")
heapq.heappush(timeline, first_event)

service_times = []
wait_times = []
in_service = False

for _ in range(100):
    # get next event from timeline
    curr_event = heapq.heappop(timeline)
    ev_time, ev_type = curr_event

    if ev_type == "arrival":
        # schedule next arrival event + next service event
        next_event = (ev_time + exp_arrival(), "arrival")
        heapq.heappush(timeline, next_event)

        if not in_service:
            next_time = ev_time + exp_service()
            heapq.heappush(timeline, (next_time, "service"))
            service_times.append(next_time - ev_time)
            wait_times.append(0)
            in_service = True
        else:
            queue.append(curr_event)
    elif ev_type == "service":
        if queue:
            queue_event = queue[0]
            queue = queue[1:]

            next_time = ev_time + exp_service()
            heapq.heappush(timeline, (next_time, "service"))
            service_times.append(next_time - queue_event[0])
            wait_times.append(ev_time - queue_event[0])
            in_service = True
        else:
            in_service = False

avg_service_time = sum(service_times)/len(service_times)
avg_wait_time = sum(wait_times)/len(wait_times)

print("avg service time, simulated={}, theoretical={}".format(avg_service_time, 1/(mu - la)))
print("avg wait time, simulated={}, theoretical={}".format(avg_wait_time, rho/(mu*(1-rho))))

