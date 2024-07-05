from services.tasks import pools_and_swimlanes_extraction, activities_from_pools_and_swimlanes_extraction

process_description = """
        Consider a process for purchasing items from an online shop. The user
        starts an order by logging in to their account. Then, the user 
        simultaneously selects the items to purchase and sets a payment
        method. Afterward, the user either pays or completes an installment 
        agreement. Since the reward value depends on the purchase value,
        After selecting the items, the user chooses between multiple options
        for a free reward. this step is done after selecting the items,
        but it is independent of the payment activities. Finally, the items
        are delivered. The user has the right to return items for exchange.
        Every time items are returned, a new delivery is made.  
    """
result = pools_and_swimlanes_extraction.evaluate(inputs={
    "process_description":process_description
})
for i in result.pools:
    print(f"Pool Name: {i["name"]}")
    for j in i["swimlanes"]:
        print(f"\t\t{j["name"]}")

activities = activities_from_pools_and_swimlanes_extraction.evaluate(inputs={
    "process_description":process_description,
    "pools_and_swimlanes":result
})

for i in activities.activities:
    print(f"Activity Name: {i["name"]}")
    print(f"Activity Pool: {i["pool"]}")
    print(f"Activity Swimlane: {i["swimlane"]}")
