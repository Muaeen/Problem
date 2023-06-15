{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "acea7f85",
   "metadata": {},
   "source": [
    "- From this problem, we need to extract the length, the slop, and also the maximum and minimum of the y coordinate\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ce50d478",
   "metadata": {},
   "outputs": [],
   "source": [
    "from math import *\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d2becae9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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Tknh01tvZeS8eUw1htzsbNexRESkBlKxe5AbX3iBwwsWcAWwICiI5HXrXEcSEZEaRsXuYdpfdRXxqan8AOR37cqcqVNdRxIRkRpExe6BQsPDmWQts+Lj6TllCk+1bes6koiI1BAqdg927+rVrJ02jdHffsvzxnDs4EHXkURExMOp2D3c4HvvJXTTJhoDm6OjWTdnjutIIiLiwVTsNUBM27aMzMlhQXAwjUeO5NXx411HEhGpfm+/DXFx4OdX8Pntt10n8kgq9hrCLyCAP2VkMO+66xjy1lv8OSyM/Lw817FERKrH22/DxImwfTtYW/B54kSVeylU7DXMr2bOZOd77zH4xAlmBQSwR1O9ioiX27NnD+mTJkF6esk70tPhoYfchPJgKvYa6NJrruGi/fs5CKRdfDGfPvus60giIpUiIyODL7/8kmnTpjF48GCioqJo2bIlwSkppT9hx47qDVgDBLgOIBVTt0EDfmMtT7Ruza8mTeLv777LpBUrXMcSESm37OxsbrvtNr744gt27NhBSEgImZmZZBdegbMfkM8ZtkSbN6++oDWEtthruD/88ANf/vGPjPrqK54xhszjx11HEhEpl/z8fPbt28f+/fsJDAwkKyurqNTvBGYAfwVOnPrE0FB4/PHqDVsDqNi9wOhHHyX/669pC6ysU4dvP//cdSQRkTILDg5m3rx5HD16lOXLl/PYY49xafv2vAr8Eujt789DwK+BXYAFshs3hunT4YYbXEb3SCp2L3FBt24MyMhgKVC3f39m3Hmn60giIuXi5+dHp06dGNCmDc998w0hwN733uO6Bx6gffv2vBcYSNuwMDKB/0yapFI/AxW7FwkMDuYRa5k9aBADnnuORxs1wubnu44lIlJm/739dhqOGMG8oCCuzc1l8DXX8Nhjj7Fx40YOHTrEjHfeIRkI05U4z0jF7oXumD+f7195hRH79/OWvz8HddaoiHg4ay1PxMYy8IUXmD18OFMzM/Hz9y/xmDp16jB06FASgaPr17sJWgOo2L1U71tuoen27QDsjo1l2auvOk4kIlK644cOMd3Pj5E7drD5pZe4fe7csz4+CTiydm31hKuBVOxerH7z5tyYl8fcRo1oM2EC/x482HUkEZESNi9cSEL9+jQAIr77jismTjzncw6Hh1P38OGqD1dDqdi9nPHz449797LozjsZsWABjxpD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\n",
      "text/plain": [
       "<Figure size 576x504 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "points = [(-10, -18), (-10, 20), (0, 3), (8, 17), (10, -16), (-10, -18)] #Selecting coordinate points\n",
    "x, y = zip(*points) #From the points, choose a ZIP function to connect the X,Y for all points.\n",
    "plt.figure(figsize=(8,7))\n",
    "plt.plot(x, y,marker='o',color='red',linewidth=1)\n",
    "plt.axhline(0, color='black',linewidth=0.5)\n",
    "plt.axvline(0, color='black',linewidth=0.5)\n",
    "    \n",
    "for i in range(len(points) - 1):    #position of arrow,coordinate and name of arrow\n",
    "    plt.arrow(x[i], y[i], x[i+1] - x[i], y[i+1] - y[i], length_includes_head=True,\n",
    "              head_width=0.7, head_length=0.5, fc='black', ec='black')\n",
    "    \n",
    "    plt.annotate(f'({x[i]}, {y[i]})', (x[i], y[i]), textcoords=\"offset points\", xytext=(-10,-15), fontsize=8)\n",
    "    \n",
    "    midpoint_x = (x[i] + x[i+1]) / 2\n",
    "    midpoint_y = (y[i] + y[i+1]) / 2\n",
    "    plt.annotate(f'V{i+1}', (midpoint_x, midpoint_y), textcoords=\"offset points\",\n",
    "                 xytext=(5,10), ha='center', fontsize=10)\n",
    "\n",
    "plt.annotate(f'({x[-1]}, {y[-1]})', (x[-1], y[-1]), textcoords=\"offset points\", xytext=(-10,-15), fontsize=8)\n",
    "\n",
    "plt.xlabel('y')\n",
    "plt.ylabel('x')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d2cee3e3",
   "metadata": {},
   "source": [
    "craete a Data Frame for all coordinate X,Y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7c9834da",
   "metadata": {},
   "outputs": [],
   "source": [
    "vectors = {    #create dictionary \n",
    "    '$x_{{1}}$': [-10,-10,0,8,10],\n",
    "    '$y_{{1}}$' : [20,20,3,17,-16],\n",
    "    '$x_{{2}}$' : [-10,0,8,10,-10],\n",
    "    '$y_{{2}}$' : [-18,3,17,-16,-18]\n",
    "}\n",
    "df = pd.DataFrame(vectors) #converte it to DataFrame\n",
    "df.set_axis(['$s_{{1}}$','$s_{{2}}$','$s_{{3}}$','$s_{{4}}$','$s_{{5}}$'],axis=0,inplace=True) #converte index to name\n",
    "df.index.name = 'vector' #name the index as vector"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3246a80f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>$x_{{1}}$</th>\n",
       "      <th>$y_{{1}}$</th>\n",
       "      <th>$x_{{2}}$</th>\n",
       "      <th>$y_{{2}}$</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>vector</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>$s_{{1}}$</th>\n",
       "      <td>-10</td>\n",
       "      <td>20</td>\n",
       "      <td>-10</td>\n",
       "      <td>-18</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>$s_{{2}}$</th>\n",
       "      <td>-10</td>\n",
       "      <td>20</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>$s_{{3}}$</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>8</td>\n",
       "      <td>17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>$s_{{4}}$</th>\n",
       "      <td>8</td>\n",
       "      <td>17</td>\n",
       "      <td>10</td>\n",
       "      <td>-16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>$s_{{5}}$</th>\n",
       "      <td>10</td>\n",
       "      <td>-16</td>\n",
       "      <td>-10</td>\n",
       "      <td>-18</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           $x_{{1}}$  $y_{{1}}$  $x_{{2}}$  $y_{{2}}$\n",
       "vector                                               \n",
       "$s_{{1}}$        -10         20        -10        -18\n",
       "$s_{{2}}$        -10         20          0          3\n",
       "$s_{{3}}$          0          3          8         17\n",
       "$s_{{4}}$          8         17         10        -16\n",
       "$s_{{5}}$         10        -16        -10        -18"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f9837d22",
   "metadata": {},
   "source": [
    "formla we are goin to is : $${c^2 = a^2 + b^2}$$\n",
    "So in this case we use : $${c^2 = (x_2 - x_1)^2 + (y_2 - y_1)^2}$$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "9170e49c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>$x_{{1}}$</th>\n",
       "      <th>$y_{{1}}$</th>\n",
       "      <th>$x_{{2}}$</th>\n",
       "      <th>$y_{{2}}$</th>\n",
       "      <th>length</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>vector</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>$s_{{1}}$</th>\n",
       "      <td>-10</td>\n",
       "      <td>20</td>\n",
       "      <td>-10</td>\n",
       "      <td>-18</td>\n",
       "      <td>38.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>$s_{{2}}$</th>\n",
       "      <td>-10</td>\n",
       "      <td>20</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>19.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>$s_{{3}}$</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>8</td>\n",
       "      <td>17</td>\n",
       "      <td>16.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>$s_{{4}}$</th>\n",
       "      <td>8</td>\n",
       "      <td>17</td>\n",
       "      <td>10</td>\n",
       "      <td>-16</td>\n",
       "      <td>33.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>$s_{{5}}$</th>\n",
       "      <td>10</td>\n",
       "      <td>-16</td>\n",
       "      <td>-10</td>\n",
       "      <td>-18</td>\n",
       "      <td>20.1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           $x_{{1}}$  $y_{{1}}$  $x_{{2}}$  $y_{{2}}$  length\n",
       "vector                                                       \n",
       "$s_{{1}}$        -10         20        -10        -18    38.0\n",
       "$s_{{2}}$        -10         20          0          3    19.7\n",
       "$s_{{3}}$          0          3          8         17    16.1\n",
       "$s_{{4}}$          8         17         10        -16    33.1\n",
       "$s_{{5}}$         10        -16        -10        -18    20.1"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['length'] = (df['$x_{{2}}$'] - df['$x_{{1}}$'])**2 + (df['$y_{{2}}$'] - df['$y_{{1}}$'])**2\n",
    "df['length'] = round(np.sqrt(df['length']),1) #round mean show numbers of numbers after decimal\n",
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bbfcba42",
   "metadata": {},
   "source": [
    "slop formla is : $$\\frac{y_{2} - y_{1}}{  x_{2} - x_{1}}$$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "2a39a6a1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>$x_{{1}}$</th>\n",
       "      <th>$y_{{1}}$</th>\n",
       "      <th>$x_{{2}}$</th>\n",
       "      <th>$y_{{2}}$</th>\n",
       "      <th>length</th>\n",
       "      <th>slop</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>vector</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>$s_{{1}}$</th>\n",
       "      <td>-10</td>\n",
       "      <td>20</td>\n",
       "      <td>-10</td>\n",
       "      <td>-18</td>\n",
       "      <td>38.0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>$s_{{2}}$</th>\n",
       "      <td>-10</td>\n",
       "      <td>20</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>19.7</td>\n",
       "      <td>-1.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>$s_{{3}}$</th>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>8</td>\n",
       "      <td>17</td>\n",
       "      <td>16.1</td>\n",
       "      <td>1.8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>$s_{{4}}$</th>\n",
       "      <td>8</td>\n",
       "      <td>17</td>\n",
       "      <td>10</td>\n",
       "      <td>-16</td>\n",
       "      <td>33.1</td>\n",
       "      <td>-16.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>$s_{{5}}$</th>\n",
       "      <td>10</td>\n",
       "      <td>-16</td>\n",
       "      <td>-10</td>\n",
       "      <td>-18</td>\n",
       "      <td>20.1</td>\n",
       "      <td>0.1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           $x_{{1}}$  $y_{{1}}$  $x_{{2}}$  $y_{{2}}$  length  slop\n",
       "vector                                                             \n",
       "$s_{{1}}$        -10         20        -10        -18    38.0   NaN\n",
       "$s_{{2}}$        -10         20          0          3    19.7  -1.7\n",
       "$s_{{3}}$          0          3          8         17    16.1   1.8\n",
       "$s_{{4}}$          8         17         10        -16    33.1 -16.5\n",
       "$s_{{5}}$         10        -16        -10        -18    20.1   0.1"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['slop'] = round((df['$y_{{2}}$']-df['$y_{{1}}$'])/(df['$x_{{2}}$']-df['$x_{{1}}$']),1)\n",
    "df['slop'] = df['slop'].replace(-np.inf, np.nan)\n",
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2071e95f",
   "metadata": {},
   "source": [
    "Max of y : $$y_{max}$$\n",
    "Minimum of y : $$y_{min}$$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "e4afe7c5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Max of y is : 20\n",
      "Minimum of y is : -18\n"
     ]
    }
   ],
   "source": [
    "only_y = list(df['$y_{{1}}$']) + list(df['$y_{{2}}$'])\n",
    "print(f'Max of y is : {max(only_y)}\\nMinimum of y is : {min(only_y)}')"
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
