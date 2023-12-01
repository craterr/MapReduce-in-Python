# Mapper-Reducer-in-Python-
Python implementation for analyzing the strike rate of a cricket batsmen using Hadoop MapReduce.

# Cricket Strike Rate Analyzer

## Repository Structure

- **Mapper Code:** [`mapper.py`](mapper.py) - Processes input data and emits intermediate key-value pairs.
- **Reducer Code:** [`reducer.py`](reducer.py) - Aggregates intermediate results and calculates the final strike rate for each batsman.
- **Sample Input:** [`sample_data.json`](sample_data.json) - Contains cricket statistics.


## Usage


1. Create an HDFS directory for input:

    ```bash
    hdfs dfs -mkdir /sr
    ```

2. Upload sample data to HDFS:

    ```bash
    hdfs dfs -put sample_data.json /sr
    ```

3. Run the Hadoop MapReduce job:

    ```bash
    hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.3.jar -mapper "$PWD/mapper.py" -reducer "$PWD/reducer.py" -input /sr/sample_data.json -output /sr/output_sr
    ```

4. View the output:

    ```bash
    hdfs dfs -ls /sr/output_sr
    hdfs dfs -cat /sr/output_sr/part-00000
    ```

## Output

```json
{"name": "Deepti", "strike_rate": 61.551}
{"name": "Harmanpreet", "strike_rate": 87.124}
{"name": "Ishan", "strike_rate": 85.077}
{"name": "Jemimah", "strike_rate": 77.407}
{"name": "Renuka", "strike_rate": 74.35}
{"name": "Rohit", "strike_rate": 71.464}
{"name": "Shubman", "strike_rate": 66.041}
{"name": "Smriti", "strike_rate": 57.807}
{"name": "VVS Laxman", "strike_rate": 64.078}
{"name": "Virat", "strike_rate": 89.928}

