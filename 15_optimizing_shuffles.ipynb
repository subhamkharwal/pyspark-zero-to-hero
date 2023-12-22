{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "67904f55-ec83-4d97-aa05-bba971265bb7",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "            <div>\n",
       "                <p><b>SparkSession - in-memory</b></p>\n",
       "                \n",
       "        <div>\n",
       "            <p><b>SparkContext</b></p>\n",
       "\n",
       "            <p><a href=\"http://4c1cbc3b031c:4040\">Spark UI</a></p>\n",
       "\n",
       "            <dl>\n",
       "              <dt>Version</dt>\n",
       "                <dd><code>v3.3.0</code></dd>\n",
       "              <dt>Master</dt>\n",
       "                <dd><code>spark://17e348267994:7077</code></dd>\n",
       "              <dt>AppName</dt>\n",
       "                <dd><code>Optimizing Shuffles</code></dd>\n",
       "            </dl>\n",
       "        </div>\n",
       "        \n",
       "            </div>\n",
       "        "
      ],
      "text/plain": [
       "<pyspark.sql.session.SparkSession at 0x7f5d3c14e890>"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Spark Session\n",
    "from pyspark.sql import SparkSession\n",
    "\n",
    "spark = (\n",
    "    SparkSession\n",
    "    .builder\n",
    "    .appName(\"Optimizing Shuffles\")\n",
    "    .master(\"spark://17e348267994:7077\")\n",
    "    .config(\"spark.cores.max\", 16)\n",
    "    .config(\"spark.executor.cores\", 4)\n",
    "    .config(\"spark.executor.memory\", \"512M\")\n",
    "    .getOrCreate()\n",
    ")\n",
    "\n",
    "spark"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "578a9878-d980-4cee-9ef9-4bd7fb0a3007",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "16"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Check Spark defaultParallelism\n",
    "\n",
    "spark.sparkContext.defaultParallelism"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b4d26dd8-c7d8-4848-9d52-ce283419dcee",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Disable AQE and Broadcast join\n",
    "\n",
    "spark.conf.set(\"spark.sql.adaptive.enabled\", False)\n",
    "spark.conf.set(\"spark.sql.adaptive.coalescePartitions.enabled\", False)\n",
    "spark.conf.set(\"spark.sql.autoBroadcastJoinThreshold\", -1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0bb7faf5-1a45-498a-8569-a16790fe06be",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Read EMP CSV file with 10M records\n",
    "\n",
    "_schema = \"first_name string, last_name string, job_title string, dob string, email string, phone string, salary double, department_id int\"\n",
    "\n",
    "emp = spark.read.format(\"csv\").schema(_schema).option(\"header\", True).load(\"/data/input/datasets/employee_records.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "70a5b553-69a6-47b0-bd58-a91b59135cff",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Find out avg salary as per dept\n",
    "from pyspark.sql.functions import avg\n",
    "\n",
    "emp_avg = emp.groupBy(\"department_id\").agg(avg(\"salary\").alias(\"avg_sal\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "b982be3b-ae76-467d-9393-81e0dedfb847",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Write data for performance Benchmarking\n",
    "\n",
    "emp_avg.write.format(\"noop\").mode(\"overwrite\").save()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "6461ffb0-1438-4e3a-a1c3-9abe96371fab",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'16'"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Check Spark Shuffle Partition setting\n",
    "\n",
    "spark.conf.get(\"spark.sql.shuffle.partitions\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "4968a5d4-817d-4eeb-9457-20d7a578fb51",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "spark.conf.set(\"spark.sql.shuffle.partitions\", 16)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "8142b4aa-5e8d-49e0-b478-79959229c611",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "+----------+----------+--------------------+----------+--------------------+--------------------+--------+-------------+------------+\n",
      "|first_name| last_name|           job_title|       dob|               email|               phone|  salary|department_id|partition_id|\n",
      "+----------+----------+--------------------+----------+--------------------+--------------------+--------+-------------+------------+\n",
      "|   Richard|  Morrison|Public relations ...|1973-05-05|melissagarcia@exa...|       (699)525-4827|512653.0|            8|           0|\n",
      "|     Bobby|  Mccarthy|   Barrister's clerk|1974-04-25|   llara@example.net|  (750)846-1602x7458|999836.0|            7|           0|\n",
      "|    Dennis|    Norman|Land/geomatics su...|1990-06-24| jturner@example.net|    873.820.0518x825|131900.0|           10|           0|\n",
      "|      John|    Monroe|        Retail buyer|1968-06-16|  erik33@example.net|    820-813-0557x624|485506.0|            1|           0|\n",
      "|  Michelle|   Elliott|      Air cabin crew|1975-03-31|tiffanyjohnston@e...|       (705)900-5337|604738.0|            8|           0|\n",
      "|    Ashley|   Montoya|        Cartographer|1976-01-16|patrickalexandra@...|        211.440.5466|483339.0|            6|           0|\n",
      "| Nathaniel|     Smith|     Quality manager|1985-06-28|  lori44@example.net|        936-403-3179|419644.0|            7|           0|\n",
      "|     Faith|  Cummings|Industrial/produc...|1978-07-01| ygordon@example.org|       (889)246-5588|205939.0|            7|           0|\n",
      "|  Margaret|    Sutton|Administrator, ed...|1975-08-16| diana44@example.net|001-647-530-5036x...|671167.0|            8|           0|\n",
      "|      Mary|    Sutton|   Freight forwarder|1979-12-28|  ryan36@example.com|   422.562.7254x3159|993829.0|            7|           0|\n",
      "|      Jake|      King|       Lexicographer|1994-07-11|monica93@example.org|+1-535-652-9715x6...|702101.0|            4|           0|\n",
      "|   Heather|     Haley|         Music tutor|1981-06-01|stephanie65@examp...|   (652)815-7973x298|570960.0|            6|           0|\n",
      "|    Thomas|    Thomas|Chartered managem...|2001-07-17|pwilliams@example...|001-245-848-0028x...|339441.0|            6|           0|\n",
      "|   Leonard|   Carlson|       Art therapist|1990-10-18|gabrielmurray@exa...|          9247590563|469728.0|            8|           0|\n",
      "|      Mark|      Wood|   Market researcher|1963-10-13|nicholas76@exampl...|   311.439.1606x3342|582291.0|            4|           0|\n",
      "|    Tracey|Washington|Travel agency man...|1986-05-07|  mark07@example.com|    001-912-206-6456|146456.0|            4|           0|\n",
      "|   Rachael| Rodriguez|         Media buyer|1966-12-02|griffinmary@examp...| +1-791-344-7586x548|544732.0|            1|           0|\n",
      "|      Tara|       Liu|   Financial adviser|1998-10-12|alexandraobrien@e...|        216.696.6061|399503.0|            3|           0|\n",
      "|       Ana|    Joseph|      Retail manager|1995-01-10|  rmorse@example.org|  (726)363-7526x9965|761988.0|           10|           0|\n",
      "|   Richard|      Hall|Engineer, civil (...|1967-03-02|brandoncardenas@e...| (964)451-9007x22496|660659.0|            4|           0|\n",
      "+----------+----------+--------------------+----------+--------------------+--------------------+--------+-------------+------------+\n",
      "only showing top 20 rows\n",
      "\n"
     ]
    }
   ],
   "source": [
    "from pyspark.sql.functions import spark_partition_id\n",
    "\n",
    "emp.withColumn(\"partition_id\", spark_partition_id()).where(\"partition_id = 0\").show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "40552990-399e-42d9-a0c9-7c920c922b71",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Read the partitioned data\n",
    "\n",
    "emp_part = spark.read.format(\"csv\").schema(_schema).option(\"header\", True).load(\"/data/input/emp_partitioned.csv/\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "707125af-139d-411e-8bc5-ce39dbfd8f36",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "emp_avg = emp_part.groupBy(\"department_id\").agg(avg(\"salary\").alias(\"avg_sal\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "650c8a41-a9eb-4fb1-b337-66ec689b0a0c",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "emp_avg.write.format(\"noop\").mode(\"overwrite\").save()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e8740183-1899-468f-bd67-af5fdb91b748",
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
   "version": "3.7.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
