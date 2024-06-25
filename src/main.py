# from tasks.actitvities_extraction import ActivityExtraction, ActivityExtractionMarker,ActivityList, ActivitySentences
# from tasks.actitvities_relationships_extraction import ActivityRelationShipsExtraction
# from llm.ollama_factory import OllamaFactory
# import json

# ollama_factory = OllamaFactory()

# task = ActivityExtraction(llm=ollama_factory.create())
# inputs={"process_description": """
#                                  Consider a process for purchasing items
#                                  from an online shop. The user starts an order by logging in to their account.
#                                  Then, the user simultaneously selects the items to purchase and sets a payment
#                                  method. Afterward, the user either pays or completes an installment agreement.
#                                  Since the reward value depends on the purchase value,
#                                  After selecting the items, the user chooses between multiple options for a free reward.
#                                  this step is done after selecting the items,
#                                  but it is independent of the payment activities.
#                                  Finally, the items are delivered. The user has the right to
#                                  return items for exchange. Every time items are returned,
#                                  a new delivery is made.
#                                """}

# result = task.handle(inputs)
# result : ActivityList = json.loads(result, object_hook=lambda d: ActivityList(**d))
# print(result)

# marks = []

# for i in result.activities:
#     print("start handling")
#     print(i)
#     print()
#     print()
#     print()
#     inner_task = ActivityExtractionMarker(ollama_factory.create())
#     relation_ship_detection = ActivityRelationShipsExtraction(ollama_factory.create())

#     relation_ship_detection_res =  relation_ship_detection.handle(
#       {"process_description": """
#                                  Consider a process for purchasing items
#                                  from an online shop. The user starts an order by logging in to their account.
#                                  Then, the user simultaneously selects the items to purchase and sets a payment
#                                  method. Afterward, the user either pays or completes an installment agreement.
#                                  Since the reward value depends on the purchase value,
#                                  After selecting the items, the user chooses between multiple options for a free reward.
#                                  this step is done after selecting the items,
#                                  but it is independent of the payment activities.
#                                  Finally, the items are delivered. The user has the right to
#                                  return items for exchange. Every time items are returned,
#                                  a new delivery is made.
#                                """,
#          "activity":i,
#          "activities":result.activities
#          }
#     )
    
#     # res=inner_task.handle(
#     #     {"process_description": """
#     #                              Consider a process for purchasing items
#     #                              from an online shop. The user starts an order by logging in to their account.
#     #                              Then, the user simultaneously selects the items to purchase and sets a payment
#     #                              method. Afterward, the user either pays or completes an installment agreement.
#     #                              Since the reward value depends on the purchase value,
#     #                              After selecting the items, the user chooses between multiple options for a free reward.
#     #                              this step is done after selecting the items,
#     #                              but it is independent of the payment activities.
#     #                              Finally, the items are delivered. The user has the right to
#     #                              return items for exchange. Every time items are returned,
#     #                              a new delivery is made.
#     #                            """,
#     #      "activity":i
#     #      })
    
#     print()
#     print()
#     print(relation_ship_detection_res)
#     # print(res)
#     # res : ActivitySentences = json.loads(res, object_hook=lambda d: ActivitySentences(**d))

#     # marks.append(res)
#     print()
#     print()
#     # print(res)
#     print()
#     print()
    
    
# print(marks)


# # crew.kickoff(inputs={"proccess_description": """
# #                                 Consider a process for purchasing items
# #                                 from an online shop. The user starts an order by logging in to their account.
# #                                 Then, the user simultaneously selects the items to purchase and sets a payment
# #                                 method. Afterward, the user either pays or completes an installment agreement.
# #                                 Since the reward value depends on the purchase value,
# #                                 After selecting the items, the user chooses between multiple options for a free reward.
# #                                 this step is done after selecting the items,
# #                                 but it is independent of the payment activities.
# #                                 Finally, the items are delivered. The user has the right to
# #                                 return items for exchange. Every time items are returned,
# #                                 a new delivery is made.
# #                               """})


# # crew.kickoff(inputs={"proccess_description": """
                                
# #                                 In the commerce application scenario, customers begin by downloading the app and
# #                                 completing the sign-up process to start their journey. They can then effortlessly browse
# #                                 through a wide range of products, thanks to a user-friendly interface equipped with
# #                                 efficient search and filter capabilities. Once they’ve made their selection,
# #                                 they place their order by adding items to their cart and proceeding to a secure checkout, 
# #                                 where they finalize their purchase through their preferred payment method. Following the transaction, 
# #                                 an automated system confirms the order and sends detailed information to the customer’s email while
# #                                 simultaneously updating the inventory levels. The warehouse team is promptly alerted to pick, pack,
# #                                 and dispatch the order for shipping, after which a courier service takes over, providing tracking details 
# #                                 to ensure transparency until delivery. Upon receiving their order, customers have the option to reach
# #                                 out to customer support for any post-purchase inquiries or assistance with returns, 
# #                                 completing the comprehensive commerce cycle.
# #                               """})


# # inputs ={"proccess_description": """
# # An e-commerce website encompasses a comprehensive and multifaceted business process that begins with user registration and authentication, where potential customers first visit the website and initiate their journey by clicking on the "Register" button. This leads them to a registration form where they are required to input various details such as their name, email address, password, and contact information. The system plays a crucial role in validating this data, ensuring that all fields are properly filled out and that the email address provided is unique within the system. To further secure the registration process, a verification email is sent to the user, containing a link they must click to confirm their email address and complete the registration. This process ensures that all registered users have valid contact information, enhancing the security and reliability of user accounts.

# # Once registered, users can proceed to log in by entering their email and password on the login page. The system cross-checks these credentials against the stored data, and upon successful authentication, users are redirected to their personalized dashboard, where they can manage their profiles, view order histories, and access other features. Meanwhile, suppliers interested in listing their products on the platform undergo a rigorous onboarding process. This involves registering on the platform, providing essential business credentials, and submitting their product catalogs. The platform conducts thorough background checks and verifies the legitimacy of the supplier's details to ensure that only reputable suppliers are allowed to list products. Approved suppliers are then granted access to the product listing interface.

# # Suppliers upload their product details, which include comprehensive descriptions, pricing information, high-quality images, and current stock levels. The system automatically checks the uploaded information for completeness and quality, ensuring that all product listings meet the platform's standards. Products are then categorized and tagged with relevant keywords to enhance their searchability on the website. Real-time inventory management is a critical component of this process. Suppliers are responsible for updating stock levels through an API or manual entry, ensuring that the system reflects accurate inventory data across all sales channels, including the website and mobile app. This integration enables automatic low-stock alerts to be sent to both suppliers and the internal procurement team, ensuring that popular items are restocked promptly to avoid stockouts.

# # Customers browsing the website can utilize sophisticated search and filter functionalities to find the products they are interested in. When users enter keywords into the search bar, the system employs advanced search algorithms, such as Elasticsearch, to match user queries with relevant product listings. The search results are displayed in a manner that prioritizes relevance, popularity, and user ratings, making it easier for customers to find what they are looking for. Additionally, users can refine their search results using various filters, such as categories, price range, brand, and customer ratings. Sorting options, including price (low to high or high to low), popularity, newest arrivals, and customer ratings, further enhance the user experience by allowing customers to organize search results according to their preferences.

# # Each product details page provides users with extensive information about the product, including detailed descriptions, specifications, pricing, availability, and delivery options. High-resolution images, 360-degree views, and videos offer customers a comprehensive visual representation of the product, helping them make informed purchase decisions. Customer reviews and ratings are prominently displayed on the product details page, allowing potential buyers to read feedback from other customers who have purchased the same product. Verified purchase tags distinguish genuine reviews from potential spam or biased comments, enhancing the credibility of the reviews.

# # When customers decide to purchase products, they add them to their shopping cart, where they can manage their selections by adjusting quantities or removing items. The system calculates the total cost, including applicable taxes and shipping fees, providing a clear and transparent breakdown of the final price. The checkout process involves several critical steps. Customers must enter or select their shipping addresses and choose from multiple payment options, including credit/debit cards, net banking, UPI, and digital wallets. The system provides a detailed order summary for the customer to review before finalizing the purchase. Once the customer confirms the order, the system processes the payment through integrated payment gateways. Successful payments trigger an order confirmation email and SMS to the customer, while failed payments prompt user notifications to retry the transaction.

# # Order processing involves coordinating with the warehouse for fulfillment. The system sends detailed order information to the warehouse, where staff receive picking lists and proceed to pack the items. Inventory levels are updated in real-time to reflect the items picked for the order. Logistics coordination plays a pivotal role in ensuring timely delivery. The system selects the appropriate shipping carrier based on factors such as delivery location, speed, and cost. Shipping details, including tracking information, are shared with the carrier, and the customer receives tracking details via email or SMS, allowing them to monitor the status of their shipment. Once the packed orders are handed over to the carrier, the system updates the order status to "shipped," and customers can track their deliveries in real-time.

# # Customer service is an essential aspect of the e-commerce business process, providing support through multiple channels, including phone, email, live chat, and social media. The support team is trained to handle inquiries related to order status, product information, returns, and other issues. When customers initiate return requests through their account portal, the system verifies the eligibility of the return based on the platform's return policy, which considers factors such as the return window and product condition. Approved return requests generate return shipping labels, and customers are instructed on how to return the items. Once the returned items are received, they undergo inspection to ensure they meet the return criteria. If the items are in sellable condition, they are restocked, and the system processes the refund, notifying the customer of the refund status.

# # Data analytics and reporting are integral to the e-commerce platform's operation, providing real-time insights into sales performance, customer behavior, and inventory management. The system generates detailed dashboards and periodic reports that help stakeholders understand key metrics such as traffic, conversion rates, average order value, and inventory turnover. Advanced analytics and machine learning algorithms analyze historical data to provide predictive insights, enabling the platform to forecast demand, optimize pricing strategies, and identify emerging trends. These insights inform strategic decisions related to inventory replenishment, marketing campaigns, and product development, ensuring that the platform remains competitive and responsive to market changes.

# # Security and compliance are paramount, with robust measures in place to protect customer data and ensure adherence to regulatory standards. Data security is maintained through encryption, secure socket layers (SSL), and access control mechanisms that restrict unauthorized access to sensitive information. Regular security audits and compliance checks are conducted to identify and address potential vulnerabilities. The platform adheres to data protection regulations such as GDPR, ensuring that customer data is handled with the utmost care and transparency. Compliance with consumer protection laws guarantees fair trade practices, dispute resolution mechanisms, and the protection of customer rights.

# # This intricate and multifaceted business process, which spans from user registration and product management to customer service and data analytics, is designed to ensure the smooth and efficient operation of an e-commerce website. By focusing on user experience, operational efficiency, security, and regulatory compliance, the platform aims to deliver exceptional value to customers, suppliers, and stakeholders, fostering a trustworthy and reliable online shopping environment.                              
# # """}
# # print(len(inputs["proccess_description"]))
# # crew.kickoff(inputs=inputs)



from mapping.mapper import Mapper
from pydantic import BaseModel

class Person(BaseModel):
    id:int
    name:str

mapper = Mapper(Person)

print(mapper)
text = """
    "identifire":1,
    "name of the person": "jack"
"""

res = mapper.map(text,"json object contains id and name for the person")
print(res)