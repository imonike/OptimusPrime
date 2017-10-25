import numpy as np
import csv
import math



print("routes array initialized")

truck_capacity = 126
quantity = (0,25,25,20,30,20,10,15,10,30,10,30,25,50,25,25)

print("quantity and truck capacity set")

customer_location = []


reader = csv.reader(open('C:\Konga\Truck_Dispatch_Solution\code\coord.csv'))
for row in reader:
	customer_location.append(row)
	
distance_matrix = np.zeros((len(customer_location),len(customer_location)))
savings_matrix = np.zeros((len(customer_location),len(customer_location)))
savings_dict = {}


print("savings array initialized")

j = 0
for i in range(len(distance_matrix)):
	j = i + 1
	while (j < len(distance_matrix[0])):
	   distance_matrix[i][j] = math.sqrt(math.pow(float(customer_location[i][1]) - float(customer_location[j][1]),2) + math.pow(float(customer_location[i][2]) - float(customer_location[j][2]),2))
	   j = j + 1 
	   
n = 1
for m in range(1,15):
	n = m + 1
	while (n <= 15):
		savings_matrix[m][n] = distance_matrix[0][m] + distance_matrix[0][n] - distance_matrix[m][n]
		nodes = "%s-%s" % (m,n)
		savings_dict[nodes] = savings_matrix[m][n]
		n = n + 1
		
		
sorted_savings = sorted(savings_dict.items(), key=lambda x: (-x[1],x[0]))
# sorted_savings = sorted(savings_dict.items(), key=lambda x: x[1])

print("sorted_savings initialized")
print(sorted_savings)

optimized_routes = []
# optimized_route1 = []
# optimized_routes.append(optimized_route1)
i = 0
current_load = 0
skipped_nodes = []
 
while len(sorted_savings) > 0:
	key = sorted_savings[i][0].split('-')
	route_end1 = int(key[0])
	route_end2 = int(key[1])
	
	print("key is %s " % (key))
	
	if len(optimized_routes) == 0:
	
		print("Inside optimized_routes is equal to 0")
        
	    
	
		if current_load + quantity[route_end1] + quantity[route_end2] < truck_capacity:
			optimized_routes.append([])
			optimized_routes[0].append(route_end1)
			optimized_routes[0].append(route_end2)
			
			current_load = current_load + quantity[route_end1] + quantity[route_end2]
	#		continue
		else :
			skipped_nodes.append(sorted_savings[i])		
	#		continue		
	elif len(optimized_routes) > 0:
	
		print("Inside optimized_routes is greater than 0")
		
	    
	
		
		outer_list_size = len(optimized_routes)
		
		print("outer list size is %s " % (outer_list_size))
		
		current_list = optimized_routes[outer_list_size-1]
		current_inner_list_size = len(optimized_routes[outer_list_size-1])
		
		print("current list is %s and the list size is %s " % (current_list,current_inner_list_size))
		
		if outer_list_size == 1:
			print("Inside outer_list_size == 1")
			if len(optimized_routes[outer_list_size-1]) >= 2:
				print("The type of key[0] and key[1] is %s " % (type(key[0])))
				print("The type of current_list[0] and current_list[current_inner_list_size-1] is %s and %s " % (type(current_list[0]),type(current_list[current_inner_list_size-1])))
				if optimized_routes[outer_list_size-1][0] == route_end1 and optimized_routes[outer_list_size-1][len(optimized_routes[outer_list_size-1])-1] == route_end2:
					print("Inside current_list[0] == route_end1 and current_list[current_inner_list_size-1] == route_end2")
					i = i + 1
					continue
				elif optimized_routes[outer_list_size-1][0] == route_end2 and optimized_routes[outer_list_size-1][len(optimized_routes[outer_list_size-1])-1] == route_end1:
					print("Inside current_list[0] == route_end2 and current_list[current_inner_list_size-1] == route_end1")
					i = i + 1
					continue
				elif optimized_routes[outer_list_size-1][0] == route_end1:
					print("Inside current_list[0] == route_end1")
					if current_load + quantity[route_end2] < truck_capacity and route_end2 not in optimized_routes[outer_list_size-1]:
						optimized_routes[outer_list_size-1].insert(0,route_end2)
						current_load = current_load + quantity[route_end2]
			#			continue
						for x in range(len(skipped_nodes)):
							skipped_key = skipped_nodes[x][0].split('-')
							route_end3 = int(skipped_key[0])
							route_end4 = int(skipped_key[1])
							
							if optimized_routes[outer_list_size-1][0] == route_end3:
								print("optimized_routes[outer_list_size-1][0] == route_end3")
								if current_load + quantity[route_end4] < truck_capacity and route_end4 not in optimized_routes[outer_list_size-1]:
									optimized_routes[outer_list_size-1].insert(0,route_end4)
									current_load = current_load + quantity[route_end4]
									
								
							elif optimized_routes[outer_list_size-1][0] == route_end4:
								print("optimized_routes[outer_list_size-1][0] == route_end4")
								if current_load + quantity[route_end3] < truck_capacity and route_end3 not in optimized_routes[outer_list_size-1]:
									optimized_routes[outer_list_size-1].insert(0,route_end3)
									current_load = current_load + quantity[route_end3]
								
							else:
								print("Nothing to do 4")
					else:
						skipped_nodes.append(sorted_savings[i])
			#			continue
					 
				elif optimized_routes[outer_list_size-1][len(optimized_routes[outer_list_size-1])-1] == route_end1:
					print("Inside current_list[current_inner_list_size-1] == route_end1")
					if current_load + quantity[route_end2] < truck_capacity and route_end2 not in optimized_routes[outer_list_size-1]:
						optimized_routes[outer_list_size-1].append(route_end2)
						current_load = current_load + quantity[route_end2]
			#		continue
						for x in range(len(skipped_nodes)):
							skipped_key = skipped_nodes[x][0].split('-')
							route_end3 = int(skipped_key[0])
							route_end4 = int(skipped_key[1])
							
							if optimized_routes[outer_list_size-1][len(optimized_routes[outer_list_size-1])-1] == route_end3:
								print("optimized_routes[outer_list_size-1][len(optimized_routes[outer_list_size-1])-1] == route_end3")
								if current_load + quantity[route_end4] < truck_capacity and route_end4 not in optimized_routes[outer_list_size-1]:
									optimized_routes[outer_list_size-1].append(route_end4)
									current_load = current_load + quantity[route_end4]
									
								
							elif optimized_routes[outer_list_size-1][len(optimized_routes[outer_list_size-1])-1] == route_end4:
								print("optimized_routes[outer_list_size-1][len(optimized_routes[outer_list_size-1])-1] == route_end4")
								if current_load + quantity[route_end3] < truck_capacity and route_end3 not in optimized_routes[outer_list_size-1]:
									optimized_routes[outer_list_size-1].append(route_end3)
									current_load = current_load + quantity[route_end3]
								
							else:
								print("Nothing to do 5")
					else:
						skipped_nodes.append(sorted_savings[i]) 
			#		continue
					 
				elif optimized_routes[outer_list_size-1][0] == route_end2:
					print("Inside current_list[0] == route_end2")
					if current_load + quantity[route_end1] < truck_capacity and route_end1 not in optimized_routes[outer_list_size-1]:
						optimized_routes[outer_list_size-1].insert(0,route_end1)
						current_load = current_load + quantity[route_end1]
			#		continue
						for x in range(len(skipped_nodes)):
							skipped_key = skipped_nodes[x][0].split('-')
							route_end3 = int(skipped_key[0])
							route_end4 = int(skipped_key[1])
							
							if optimized_routes[outer_list_size-1][0] == route_end3:
								print("optimized_routes[outer_list_size-1][0] == route_end3")
								if current_load + quantity[route_end4] < truck_capacity and route_end4 not in optimized_routes[outer_list_size-1]:
									optimized_routes[outer_list_size-1].insert(0,route_end4)
									current_load = current_load + quantity[route_end4]
									
								
							elif optimized_routes[outer_list_size-1][0] == route_end4:
								print("optimized_routes[outer_list_size-1][0] == route_end4")
								if current_load + quantity[route_end3] < truck_capacity and route_end3 not in optimized_routes[outer_list_size-1]:
									optimized_routes[outer_list_size-1].insert(0,route_end3)
									current_load = current_load + quantity[route_end3]
								
							else:
								print("Nothing to do 6")
					else:
						skipped_nodes.append(sorted_savings[i])
			#		continue
					
				elif optimized_routes[outer_list_size-1][len(optimized_routes[outer_list_size-1])-1] == route_end2:
					print("Inside current_list[current_inner_list_size-1] == route_end2")
					if current_load + quantity[route_end1] < truck_capacity and route_end1 not in optimized_routes[outer_list_size-1]:
						optimized_routes[outer_list_size-1].append(route_end1)
						current_load = current_load + quantity[route_end1]
			#		continue
						for x in range(len(skipped_nodes)):
							skipped_key = skipped_nodes[x][0].split('-')
							route_end3 = int(skipped_key[0])
							route_end4 = int(skipped_key[1])
							
							if optimized_routes[outer_list_size-1][len(optimized_routes[outer_list_size-1])-1] == route_end3:
								print("optimized_routes[outer_list_size-1][len(optimized_routes[outer_list_size-1])-1] == route_end3")
								if current_load + quantity[route_end4] < truck_capacity and route_end4 not in optimized_routes[outer_list_size-1]:
									optimized_routes[outer_list_size-1].append(route_end4)
									current_load = current_load + quantity[route_end4]
									
								
							elif optimized_routes[outer_list_size-1][len(optimized_routes[outer_list_size-1])-1] == route_end4:
								print("optimized_routes[outer_list_size-1][len(optimized_routes[outer_list_size-1])-1] == route_end4")
								if current_load + quantity[route_end3] < truck_capacity and route_end3 not in optimized_routes[outer_list_size-1]:
									optimized_routes[outer_list_size-1].append(route_end3)
									current_load = current_load + quantity[route_end3]
								
							else:
								print("Nothing to do 7")
					else:
						skipped_nodes.append(sorted_savings[i])
			#		continue
				else :
			#	continue
					print ("Nothing to do 1")
					skipped_nodes.append(sorted_savings[i])
			else:
				if current_load + quantity[route_end1] + quantity[route_end2] < truck_capacity:
					optimized_routes[outer_list_size-1].append(route_end1)
					optimized_routes[outer_list_size-1].append(route_end2)
				
					current_load = current_load + quantity[route_end1] + quantity[route_end2]
		#		continue
				
				else:
					skipped_nodes.append(sorted_savings[i])		
		#		continue
		else:
			print("Inside outer_list_size > 1")
			previous_list = optimized_routes[outer_list_size-2]
			print("previous list is %s and its type is %s " % (previous_list, type(previous_list)))
			
			
				
			if route_end1 in previous_list or route_end2 in previous_list:
				print("Inside break")
					
			else:
					
				if current_inner_list_size >= 2:
					print("The type of key[0] and key[1] is %s " % (type(key[0])))
					print("The type of current_list[0] and current_list[current_inner_list_size-1] is %s and %s " % (type(current_list[0]),type(current_list[current_inner_list_size-1])))
					if current_list[0] == route_end1 and current_list[current_inner_list_size-1] == route_end2:
						print("Inside current_list[0] == route_end1 and current_list[current_inner_list_size-1] == route_end2")
						i = i + 1
						continue
					elif current_list[0] == route_end2 and current_list[current_inner_list_size-1] == route_end1:
						print("Inside current_list[0] == route_end2 and current_list[current_inner_list_size-1] == route_end1")
						i = i + 1
						continue
					elif optimized_routes[outer_list_size-1][0] == route_end1:
						print("Inside current_list[0] == route_end1")
						if current_load + quantity[route_end2] < truck_capacity and route_end2 not in optimized_routes[outer_list_size-1]:
							optimized_routes[outer_list_size-1].insert(0,route_end2)
							current_load = current_load + quantity[route_end2]
			#			continue
							for x in range(len(skipped_nodes)):
								skipped_key = skipped_nodes[x][0].split('-')
								route_end3 = int(skipped_key[0])
								route_end4 = int(skipped_key[1])
							
								if optimized_routes[outer_list_size-1][0] == route_end3:
									print("optimized_routes[outer_list_size-1][0] == route_end3")
									if current_load + quantity[route_end4] < truck_capacity and route_end4 not in optimized_routes[outer_list_size-1]:
										optimized_routes[outer_list_size-1].insert(0,route_end4)
										current_load = current_load + quantity[route_end4]
									
								
								elif optimized_routes[outer_list_size-1][0] == route_end4:
									print("optimized_routes[outer_list_size-1][0] == route_end4")
									if current_load + quantity[route_end3] < truck_capacity and route_end3 not in optimized_routes[outer_list_size-1]:
										optimized_routes[outer_list_size-1].insert(0,route_end3)
										current_load = current_load + quantity[route_end3]
								
								else:
									print("Nothing to do 8")
						else:
							skipped_nodes.append(sorted_savings[i])
			#			continue
					 
					elif optimized_routes[outer_list_size-1][len(optimized_routes[outer_list_size-1])-1] == route_end1:
						print("Inside current_list[current_inner_list_size-1] == route_end1")
						if current_load + quantity[route_end2] < truck_capacity and route_end2 not in optimized_routes[outer_list_size-1]:
							optimized_routes[outer_list_size-1].append(route_end2)
							current_load = current_load + quantity[route_end2]
			#		continue
							for x in range(len(skipped_nodes)):
								skipped_key = skipped_nodes[x][0].split('-')
								route_end3 = int(skipped_key[0])
								route_end4 = int(skipped_key[1])
							
								if optimized_routes[outer_list_size-1][len(optimized_routes[outer_list_size-1])-1] == route_end3:
									print("optimized_routes[outer_list_size-1][len(optimized_routes[outer_list_size-1])-1] == route_end3")
									if current_load + quantity[route_end4] < truck_capacity and route_end4 not in optimized_routes[outer_list_size-1]:
										optimized_routes[outer_list_size-1].append(route_end4)
										current_load = current_load + quantity[route_end4]
									
								
								elif optimized_routes[outer_list_size-1][len(optimized_routes[outer_list_size-1])-1] == route_end4:
									print("optimized_routes[outer_list_size-1][len(optimized_routes[outer_list_size-1])-1] == route_end4")
									if current_load + quantity[route_end3] < truck_capacity and route_end3 not in optimized_routes[outer_list_size-1]:
										optimized_routes[outer_list_size-1].append(route_end3)
										current_load = current_load + quantity[route_end3]
								
								else:
									print("Nothing to do 9")
						else:
							skipped_nodes.append(sorted_savings[i]) 
			#		continue
					 
					elif optimized_routes[outer_list_size-1][0] == route_end2:
						print("Inside current_list[0] == route_end2")
						if current_load + quantity[route_end1] < truck_capacity and route_end1 not in optimized_routes[outer_list_size-1]:
							optimized_routes[outer_list_size-1].insert(0,route_end1)
							current_load = current_load + quantity[route_end1]
			#		continue
							for x in range(len(skipped_nodes)):
								skipped_key = skipped_nodes[x][0].split('-')
								route_end3 = int(skipped_key[0])
								route_end4 = int(skipped_key[1])
							
								if optimized_routes[outer_list_size-1][0] == route_end3:
									print("optimized_routes[outer_list_size-1][0] == route_end3")
									if current_load + quantity[route_end4] < truck_capacity and route_end4 not in optimized_routes[outer_list_size-1]:
										optimized_routes[outer_list_size-1].insert(0,route_end4)
										current_load = current_load + quantity[route_end4]
									
								
								elif optimized_routes[outer_list_size-1][0] == route_end4:
									print("optimized_routes[outer_list_size-1][0] == route_end4")
									if current_load + quantity[route_end3] < truck_capacity and route_end3 not in optimized_routes[outer_list_size-1]:
										optimized_routes[outer_list_size-1].insert(0,route_end3)
										current_load = current_load + quantity[route_end3]
								
								else:
									print("Nothing to do 10")
						else:
								skipped_nodes.append(sorted_savings[i])
			#		continue
					
					elif optimized_routes[outer_list_size-1][len(optimized_routes[outer_list_size-1])-1] == route_end2:
						print("Inside current_list[current_inner_list_size-1] == route_end2")
						if current_load + quantity[route_end1] < truck_capacity and route_end1 not in optimized_routes[outer_list_size-1]:
							optimized_routes[outer_list_size-1].append(route_end1)
							current_load = current_load + quantity[route_end1]
			#		continue
							for x in range(len(skipped_nodes)):
								skipped_key = skipped_nodes[x][0].split('-')
								route_end3 = int(skipped_key[0])
								route_end4 = int(skipped_key[1])
							
								if optimized_routes[outer_list_size-1][len(optimized_routes[outer_list_size-1])-1] == route_end3:
									print("optimized_routes[outer_list_size-1][len(optimized_routes[outer_list_size-1])-1] == route_end3")
									if current_load + quantity[route_end4] < truck_capacity and route_end4 not in optimized_routes[outer_list_size-1]:
										optimized_routes[outer_list_size-1].append(route_end4)
										current_load = current_load + quantity[route_end4]
									
								
								elif optimized_routes[outer_list_size-1][len(optimized_routes[outer_list_size-1])-1] == route_end4:
									print("optimized_routes[outer_list_size-1][len(optimized_routes[outer_list_size-1])-1] == route_end4")
									if current_load + quantity[route_end3] < truck_capacity and route_end3 not in optimized_routes[outer_list_size-1]:
										optimized_routes[outer_list_size-1].append(route_end3)
										current_load = current_load + quantity[route_end3]
								
								else:
									print("Nothing to do 11")
						else:
							skipped_nodes.append(sorted_savings[i])
			#		continue
					else :
			#	continue
						print ("Nothing to do 2")
						skipped_nodes.append(sorted_savings[i])
				else:
					print("Inside current_inner_list_size < 2")
					if current_load + quantity[route_end1] + quantity[route_end2] < truck_capacity:
						optimized_routes[outer_list_size-1].append(route_end1)
						optimized_routes[outer_list_size-1].append(route_end2)
				
						current_load = current_load + quantity[route_end1] + quantity[route_end2]
		#		continue
				
					else:
						skipped_nodes.append(sorted_savings[i])		
		#		continue
					
					
	else:	
	#	continue
		print("Nothing to do 3")
		 
	if i == len(sorted_savings) - 1:
		print("Finished going through sorted_savings array about to print skipped nodes")
		if len(skipped_nodes) > 0:
			sorted_savings = skipped_nodes
			print("skipped nodes: %s" % (skipped_nodes))
			skipped_nodes = []
			optimized_routes.append([])
			i = 0
			current_load = 0
		else:
			sorted_savings = skipped_nodes 
	else:
		i = i + 1
		print("i is equal to: %s" % i)

print optimized_routes	

	     

