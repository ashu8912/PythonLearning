print(".....rock.....");
print(".....paper.....");
print(".....scissor.....");

player1_hit=input("hey player 1 enter your hit");
print("No_CHEATING\n\n"*30);
player2_hit=input("hey player 2 enter your hit");

if(player1_hit==player2_hit):
	print("this is a tie");
elif(player1_hit=="rock"):
 	if(player2_hit=="scissor"):
 		print("player1 you have won");
 	if(player2_hit=="paper"):
 		print("player2 you have won");
elif(player1_hit=="paper"):
	if(player2_hit=="scissor"):
		print("player2 you have won");
	if(player2_hit=="rock"):
		print("player1 you have won");
elif(player1_hit=="scissor"):
	if(player2_hit=="paper"):
		print("player1 you have won");
	if(player2_hit=="rock"):
		print("player2 you have won");

else:
	print("you have entered something incorrect");							 			