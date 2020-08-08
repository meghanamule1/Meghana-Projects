{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Round : 1\n",
      "Player 1 Rolls : 2\n",
      "Player 2 Rolls : 3\n",
      "Player 2 : wins!\n",
      "Round : 2\n",
      "Player 1 Rolls : 1\n",
      "Player 2 Rolls : 2\n",
      "Player 2 : wins!\n",
      "Round : 3\n",
      "Player 1 Rolls : 1\n",
      "Player 2 Rolls : 2\n",
      "Player 2 : wins!\n",
      "Round : 4\n",
      "Player 1 Rolls : 6\n",
      "Player 2 Rolls : 5\n",
      "Player 1 : wins!\n",
      "Round : 5\n",
      "Player 1 Rolls : 3\n",
      "Player 2 Rolls : 1\n",
      "Player 1 : wins!\n",
      "Round : 6\n",
      "Player 1 Rolls : 3\n",
      "Player 2 Rolls : 6\n",
      "Player 2 : wins!\n",
      "Round : 7\n",
      "Player 1 Rolls : 5\n",
      "Player 2 Rolls : 3\n",
      "Player 1 : wins!\n",
      "Round : 8\n",
      "Player 1 Rolls : 1\n",
      "Player 2 Rolls : 2\n",
      "Player 2 : wins!\n",
      "Round : 9\n",
      "Player 1 Rolls : 3\n",
      "Player 2 Rolls : 1\n",
      "Player 1 : wins!\n",
      "Round : 10\n",
      "Player 1 Rolls : 5\n",
      "Player 2 Rolls : 1\n",
      "Player 1 : wins!\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "def main():\n",
    "    player1= 0\n",
    "    player1wins=0\n",
    "    player2= 0\n",
    "    player2wins=0\n",
    "    rounds=1\n",
    "\n",
    "    while rounds !=11:\n",
    "        print(\"Round : \" + str(rounds))\n",
    "        player1 = dice_roll()\n",
    "        player2 = dice_roll()\n",
    "        print(\"Player 1 Rolls : \" + str(player1))\n",
    "        print(\"Player 2 Rolls : \" + str(player2))\n",
    "\n",
    "        if(player1 == player2):\n",
    "            print(\"Draw!\")\n",
    "        elif(player1 > player2):\n",
    "            player1wins = player1wins +1\n",
    "            print(\"Player 1 : wins!\")\n",
    "        else:\n",
    "            player2wins = player2wins +1\n",
    "            print(\"Player 2 : wins!\")\n",
    "\n",
    "        rounds= rounds + 1\n",
    "\n",
    "def dice_roll():\n",
    "    diceroll= random.randint(1,6)\n",
    "    return diceroll\n",
    "\n",
    "main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
