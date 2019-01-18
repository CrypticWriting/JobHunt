{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Jobhunt stats of 2018 - matplotlib, pandas & numpy"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "With this file I'm playing around with some jobhunt stats from the 2018.\n",
    "Stats include the company, time of application and if  interview took place.\n",
    "\n",
    "On this file I'm using matplotlib, pyplot, numpy and pandas."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd \n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "\n",
    "df = pd.read_csv(\n",
    "    \"jobhunt.csv\",\n",
    "    delimiter=\";\"\n",
    "    )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Investigating and modifying dataframe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
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
       "      <th>Unnamed: 0</th>\n",
       "      <th>company</th>\n",
       "      <th>time</th>\n",
       "      <th>interviewed</th>\n",
       "      <th>Unnamed: 4</th>\n",
       "      <th>Unnamed: 5</th>\n",
       "      <th>Unnamed: 6</th>\n",
       "      <th>Unnamed: 7</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>147</th>\n",
       "      <td>148.0</td>\n",
       "      <td>Logentia</td>\n",
       "      <td>2018-12-10</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>148</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>149</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>150</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>151</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Unnamed: 0   company        time interviewed  Unnamed: 4  Unnamed: 5  \\\n",
       "147       148.0  Logentia  2018-12-10         NaN         NaN         NaN   \n",
       "148         NaN       NaN         NaN         NaN         NaN         NaN   \n",
       "149         NaN       NaN         NaN         NaN         NaN         NaN   \n",
       "150         NaN       NaN         NaN         NaN         NaN         NaN   \n",
       "151         NaN       NaN         NaN         NaN         NaN         NaN   \n",
       "\n",
       "     Unnamed: 6  Unnamed: 7  \n",
       "147         NaN         NaN  \n",
       "148         NaN         NaN  \n",
       "149         NaN         NaN  \n",
       "150         NaN         NaN  \n",
       "151         NaN         NaN  "
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.tail(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Unnamed: 0       4\n",
       "company          4\n",
       "time             4\n",
       "interviewed    132\n",
       "Unnamed: 4     152\n",
       "Unnamed: 5     152\n",
       "Unnamed: 6     152\n",
       "Unnamed: 7     152\n",
       "dtype: int64"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# CHECKING nan values from dataframe\n",
    "\n",
    "df.isna().sum()\n",
    "\n",
    "# -> it appears that the end of the dataframe has nan values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# DROPPING nan values from selected column and saving data to a new variable\n",
    "\n",
    "df.dropna(\n",
    "    subset=[\"company\", \"time\"], \n",
    "    how=\"any\",\n",
    "    inplace=True\n",
    "    )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
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
       "      <th>Unnamed: 0</th>\n",
       "      <th>company</th>\n",
       "      <th>time</th>\n",
       "      <th>interviewed</th>\n",
       "      <th>Unnamed: 4</th>\n",
       "      <th>Unnamed: 5</th>\n",
       "      <th>Unnamed: 6</th>\n",
       "      <th>Unnamed: 7</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>145</th>\n",
       "      <td>146.0</td>\n",
       "      <td>valtiolle</td>\n",
       "      <td>2018-12-04</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>146</th>\n",
       "      <td>147.0</td>\n",
       "      <td>Upseller</td>\n",
       "      <td>2018-12-05</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>147</th>\n",
       "      <td>148.0</td>\n",
       "      <td>Logentia</td>\n",
       "      <td>2018-12-10</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Unnamed: 0    company        time interviewed  Unnamed: 4  Unnamed: 5  \\\n",
       "145       146.0  valtiolle  2018-12-04         NaN         NaN         NaN   \n",
       "146       147.0   Upseller  2018-12-05         NaN         NaN         NaN   \n",
       "147       148.0   Logentia  2018-12-10         NaN         NaN         NaN   \n",
       "\n",
       "     Unnamed: 6  Unnamed: 7  \n",
       "145         NaN         NaN  \n",
       "146         NaN         NaN  \n",
       "147         NaN         NaN  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"\"\"CHECKING how the end of our dataframe looks like\n",
    "- column \"interviewed\" can still have nan values\"\"\"\n",
    "\n",
    "df.tail(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Unnamed: 0       0\n",
       "company          0\n",
       "time             0\n",
       "interviewed    128\n",
       "Unnamed: 4     148\n",
       "Unnamed: 5     148\n",
       "Unnamed: 6     148\n",
       "Unnamed: 7     148\n",
       "dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"\"\"DOUBLE checking with the table that nan values \n",
    "aren't amon, mainly \"time\"-column\"\"\"\n",
    "\n",
    "df.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"SPLITTING time -column to month-only\n",
    "This way we can use it to group dataset by month\"\"\"\n",
    "\n",
    "df['time'] = df.time.apply(lambda x: x.split('-')[-2])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Setting data ready for plotting"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3, 4, 22, 30, 17, 15, 9, 25, 18, 5]\n",
      "[3, 4, 22, 30, 17, 15, 9, 25, 18, 0, 0, 5]\n",
      "[1, 2, 3, 4, 5, 6, 7, 8, 9, 12]\n",
      "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]\n"
     ]
    }
   ],
   "source": [
    "# Outputting \"time\"-column to a list for month_applied -variable\n",
    "\n",
    "application_per_month = \\\n",
    "    df.groupby(\"time\")\\\n",
    "    .time.count()\\\n",
    "    .tolist()\n",
    "\n",
    "\n",
    "# Appending missing values to compleate the whole year\n",
    "\n",
    "all_application_per_month = \\\n",
    "    application_per_month[:9] \\\n",
    "    + [0,0] \\\n",
    "    + application_per_month[9:]\n",
    "\n",
    "\n",
    "\"\"\"OUTPUTTING unique values from time to months_grouped_to_months \n",
    "also coz the output of unique() is a float we change it to type int \n",
    "and list\"\"\"\n",
    "\n",
    "months_grouped_to_months = \\\n",
    "    df.time.unique()\\\n",
    "    .astype(int)\\\n",
    "    .tolist()\n",
    "\n",
    "\n",
    "\"\"\"APPENDING missing month values to complete the whole year on \n",
    "all_months_grouped_to_months\"\"\"\n",
    "\n",
    "all_months_grouped_to_months = \\\n",
    "    months_grouped_to_months[:9] \\\n",
    "    + [10,11] \\\n",
    "    + months_grouped_to_months[9:]\n",
    "\n",
    "\n",
    "\"\"\"WILL count the highest month and adds +5 - just testing some\n",
    "highest_values = df[\"aika\"].astype(int).max() \n",
    "print(highest_values + 5)\"\"\"\n",
    "\n",
    "print(application_per_month)\n",
    "print(all_application_per_month)\n",
    "\n",
    "print(months_grouped_to_months)\n",
    "print(all_months_grouped_to_months)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
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
       "      <th>Unnamed: 0</th>\n",
       "      <th>company</th>\n",
       "      <th>time</th>\n",
       "      <th>interviewed</th>\n",
       "      <th>Unnamed: 4</th>\n",
       "      <th>Unnamed: 5</th>\n",
       "      <th>Unnamed: 6</th>\n",
       "      <th>Unnamed: 7</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>145</th>\n",
       "      <td>146.0</td>\n",
       "      <td>valtiolle</td>\n",
       "      <td>12</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>146</th>\n",
       "      <td>147.0</td>\n",
       "      <td>Upseller</td>\n",
       "      <td>12</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>147</th>\n",
       "      <td>148.0</td>\n",
       "      <td>Logentia</td>\n",
       "      <td>12</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Unnamed: 0    company time interviewed  Unnamed: 4  Unnamed: 5  \\\n",
       "145       146.0  valtiolle   12         NaN         NaN         NaN   \n",
       "146       147.0   Upseller   12         NaN         NaN         NaN   \n",
       "147       148.0   Logentia   12         NaN         NaN         NaN   \n",
       "\n",
       "     Unnamed: 6  Unnamed: 7  \n",
       "145         NaN         NaN  \n",
       "146         NaN         NaN  \n",
       "147         NaN         NaN  "
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.tail(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 0, 1, 3, 2, 4, 1, 3, 6, 0]\n",
      "[0, 0, 1, 3, 2, 4, 1, 3, 6, 0, 0, 0]\n"
     ]
    }
   ],
   "source": [
    "# SETTING interviewed column ready for plotting\n",
    "\n",
    "was_interviewed = \\\n",
    "    df.groupby(\"time\")\\\n",
    "    .interviewed\\\n",
    "    .count()\\\n",
    "    .tolist()\n",
    "\n",
    "print(was_interviewed)\n",
    "\n",
    "\n",
    "# APPENDING missing months to a list\n",
    "\n",
    "october_november = [0,0]\n",
    "\n",
    "was_interviewed_all_months = \\\n",
    "    was_interviewed[:9] \\\n",
    "    + october_november \\\n",
    "    + was_interviewed[9:]\n",
    "\n",
    "print(was_interviewed_all_months)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Plotting the data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# PLOTTING the whole thingamathing with matplotlib\n",
    "\n",
    "plt.plot(\n",
    "        all_months_grouped_to_months, \n",
    "        all_application_per_month, \n",
    "        color=\"darkgreen\", marker=\"o\"\n",
    "        )\n",
    "\n",
    "\n",
    "plt.plot(\n",
    "        all_months_grouped_to_months, \n",
    "        was_interviewed_all_months, \n",
    "        color=\"blue\", linestyle=\"--\"\n",
    "        )\n",
    "\n",
    "\n",
    "plt.title(\"Jobhunt 2018\")\n",
    "plt.xlabel(\"Months\")\n",
    "plt.ylabel(\"Amount of applications per month\")\n",
    "legend_label = [\"Applications\", \"Interfiew\"]\n",
    "\n",
    "\n",
    "plt.legend(legend_label, loc=1)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/matiaspehkonen/anaconda3/lib/python3.7/site-packages/matplotlib/cbook/deprecation.py:107: MatplotlibDeprecationWarning: Adding an axes using the same arguments as a previous axes currently reuses the earlier instance.  In a future version, a new instance will always be created and returned.  Meanwhile, this warning can be suppressed, and the future behavior ensured, by passing a unique label to each axes instance.\n",
      "  warnings.warn(message, mplDeprecation, stacklevel=1)\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# JUST another df focusing bit more for the design\n",
    "\n",
    "plt.plot(\n",
    "        all_months_grouped_to_months, \n",
    "        all_application_per_month, \n",
    "        color=\"purple\", \n",
    "        marker=\"o\"\n",
    "        )\n",
    "\n",
    "\n",
    "plt.bar(\n",
    "        all_months_grouped_to_months, \n",
    "        all_application_per_month, \n",
    "        color=\"lightgray\"\n",
    "       )\n",
    "\n",
    "\n",
    "plt.plot(\n",
    "        all_months_grouped_to_months, \n",
    "        was_interviewed_all_months, \n",
    "        color=\"darkblue\", \n",
    "        linestyle=\"--\", \n",
    "        marker=\"o\"\n",
    "        )\n",
    "\n",
    "# SETTING new names for xticks\n",
    "month_names = [\n",
    "    \"Jan\", \"Feb\", \"Mar\", \n",
    "    \"Apr\", \"May\", \"Jun\", \n",
    "    \"Jul\", \"Aug\", \"Sep\", \n",
    "    \"Oct\", \"Nov\", \"Dec\"\n",
    "    ]\n",
    "\n",
    "\n",
    "# MAKING things neat\n",
    "plt.title(\"Jobhunt 2018\")\n",
    "plt.xlabel(\"Months\")\n",
    "plt.ylabel(\"Amount of applications per month\")\n",
    "\n",
    "legend_label = [\"Applications\", \"Interfiew\"]\n",
    "plt.legend(legend_label, loc=1)\n",
    "\n",
    "ax = plt.subplot()\n",
    "ax.set_xticks(all_months_grouped_to_months)\n",
    "ax.set_xticklabels(month_names, rotation=30)\n",
    "\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0,0.5,'Plot two')"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# SHOWING off with mad subplot skills with first plot\n",
    "\n",
    "plt.subplot(2, 1, 1)\n",
    "\n",
    "plt.bar(\n",
    "    all_months_grouped_to_months, all_application_per_month, \n",
    "    color=\"purple\"\n",
    "    )\n",
    "\n",
    "\n",
    "# TITLE and label for the first plot\n",
    "\n",
    "plt.title(\"Job applications\")\n",
    "plt.ylabel(\"Plot one\")\n",
    "\n",
    "\n",
    "# SECOND plot amazing plot\n",
    "\n",
    "plt.subplot(2, 1, 2)\n",
    "plt.subplots_adjust(hspace=0.75)\n",
    "\n",
    "plt.bar(\n",
    "    all_months_grouped_to_months, \n",
    "    was_interviewed_all_months, \n",
    "    color=\"darkred\" \n",
    "    )\n",
    "\n",
    "\n",
    "# TITLE and label for the second plot\n",
    "\n",
    "plt.title(\"Interviews\")\n",
    "plt.ylabel(\"Plot two\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Playing around with pie chart"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x576 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "\"\"\"TRYING first to create pie with pre-existing\n",
    "values, but noticed there are zeroes involved.\n",
    "\n",
    "So first I needed to delete zero's from the list, \n",
    "but then the label got too long, so went on did\n",
    "the slice editing for the values on labels as well\"\"\"\n",
    "\n",
    "# REMOVING zero's from the list with numpy\n",
    "\n",
    "zero_removed_from_application_list =  \\\n",
    "    np.array([all_application_per_month]) \\\n",
    "    [(np.array([all_application_per_month]) \\\n",
    "    > 0)].astype(int).tolist()\n",
    "\n",
    "# PRINTING values to check them\n",
    "# print(zero_removed_from_application_list)\n",
    "\n",
    "\n",
    "# SPLITTING month_names to new superduber_list variable\n",
    "\n",
    "month_names_one = month_names[0:9]\n",
    "month_names_two = month_names[-1:]\n",
    "\n",
    "superduber_list = month_names_one + month_names_two\n",
    "\n",
    "# MAKING sure that he values are ok\n",
    "# print(superduber)\n",
    "\n",
    "\n",
    "# POSITIONIN piechart\n",
    "\n",
    "plt.figure(figsize=(10, 8))\n",
    "\n",
    "\n",
    "# PLOTTING pie\n",
    "plt.pie(\n",
    "    zero_removed_from_application_list,\n",
    "    labels=superduber_list, \\\n",
    "    autopct=\"%d%%\"\n",
    "    )\n",
    "\n",
    "\n",
    "plt.axis(\"equal\")\n",
    "plt.title(\"This is how effort scattered trough out the year\")\n",
    "plt.show()\n",
    "\n",
    "# WANNA save? -> plt.savefig(\"my_pie_chart.png\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Few lines on statistics"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The median of the applications is: 12.0\n",
      "The mean, 12.3, is also a good number per month.\n",
      "I don't know what is the use of std at this dataset, but I suppose it represents that I can count standard deviation: 9.8 as well.\n"
     ]
    }
   ],
   "source": [
    "# MEDIAN of the values - rounded to 0 decimals\n",
    "\n",
    "median_all_application_per_month =\\\n",
    "    np.median(all_application_per_month)\\\n",
    "    .round(decimals=0)\n",
    "\n",
    "# PRINT median\n",
    "\n",
    "print(\n",
    "    \"The median of the applications is: {}\"\\\n",
    "    .format(median_all_application_per_month)\n",
    "    )\n",
    "\n",
    "\n",
    "# MEAN calculations - rounding value to 1 decimal\n",
    "\n",
    "mean_all_application_per_month =\\\n",
    "    np.mean(all_application_per_month)\\\n",
    "    .round(decimals=1)\n",
    "\n",
    "# PRINT mean\n",
    "\n",
    "print(\"The mean, %s, is also a good number per month.\"\\\n",
    "    % mean_all_application_per_month)\n",
    "\n",
    "\n",
    "\"\"\"STANDARD deviation aka the avg distance \n",
    "of the values \n",
    "from the mean - rounding value to 1 decimal\"\"\"\n",
    "\n",
    "std_all_application_per_month =\\\n",
    "    np.std(all_application_per_month)\\\n",
    "    .round(decimals=1)\n",
    "\n",
    "# PRINT STD - I think this is not the prettiest way to split the text input\n",
    "\n",
    "print(\n",
    "    \"I don't know what is the use of std at this \" \\\n",
    "    + \"dataset, but I suppose it represents that \" \\\n",
    "    + \"I can count standard deviation: \" \\\n",
    "    + str(std_all_application_per_month) \\\n",
    "    + \" as well.\"\n",
    "    )\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
