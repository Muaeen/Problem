{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "bf0d1373",
   "metadata": {},
   "source": [
    "# Implementing Comparative Algorithms in Python\n",
    "***\n",
    "\n",
    "you'll be learning how to write a **Python** program that takes three numbers as input, compares them, and then outputs the largest of the three numbers. If all three numbers are equal, it will inform the user of this. This program will help you understand how to implement basic comparison and control flow in Python.\n",
    "\n",
    "- STEPS WHAT I DID\n",
    "    1. Import the necessary libraries\n",
    "    2. Create a def function  :\n",
    "        - Function Declaration.\n",
    "        - Creating a List.\n",
    "        - Statement :\n",
    "            - If. \n",
    "            - Else.\n",
    "        \n",
    "        \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a15d2526",
   "metadata": {},
   "outputs": [],
   "source": [
    "from math import *  \n",
    "import numpy as np "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "53f7b0c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "def enter_num(a,b,c): # takes three parameters a, b, and c\n",
    "    liist=list([a,b,c])  # creates a list for three parameters\n",
    "    if a==b or b==c or c==a : # if statement if a or b or c equal to any parameter\n",
    "        print(f'Entered numbers are equal\\na: {a} b: {b} c: {c}')\n",
    "    else : # else statement\n",
    "        print(f'The largest of the three numbers is : {max(liist)}') # Printing maximum value from the list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "2bcb515a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Entered numbers are equal\n",
      "a: 1 b: 1 c: 1\n"
     ]
    }
   ],
   "source": [
    "enter_num(1,1,1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "3ddb6e04",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The largest of the three numbers is : 8\n"
     ]
    }
   ],
   "source": [
    "enter_num(1,5,8)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
