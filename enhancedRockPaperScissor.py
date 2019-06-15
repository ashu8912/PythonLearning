import random;

rand_num=random.randint(0,2);

if(rand_num==0):
	ai_hit="rock";
elif(rand_num==1):
  	ai_hit="paper";
else:
	ai_hit="scissor";

player1_hit=input("player choose your hit\n").lower();
if(player1_hit==ai_hit):
	print("This is a tie");
elif(player1_hit=="rock"):
	if(ai_hit=="paper"):
		print("ai choose paper and it won");
	else:
		print("ai choose scissor and it lost,You WON");
elif(player1_hit=="paper"):
 	if(ai_hit=="scissor"):
 		print("ai choose scissor and you lost");
 	else:
 		print("ai choose rock and it lost,YOU WON");
elif(player1_hit=="scissor"):
	if(ai_hit=="rock"):
		print("ai choose rock and it won");
	else:
		print("ai choose paper and it lost,YOU WON");	
else:
	print("something went wrong");			 							  		