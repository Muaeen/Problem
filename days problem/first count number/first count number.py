{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "ff038a2e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n"
     ]
    }
   ],
   "source": [
    "arr = [1,2,7,5,8,2,1]\n",
    "for i in arr:\n",
    "    if arr.count(i) == True:\n",
    "        print(i)\n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "7fda7892",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def first_num(array) :\n",
    "    for i in array:\n",
    "        if array.count(i) == 1 :\n",
    "            return i\n",
    "arr = [1,2,7,5,8,2,1]\n",
    "first_num(arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6207a769",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d7f28ede",
   "metadata": {},
   "outputs": [],
   "source": []
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
