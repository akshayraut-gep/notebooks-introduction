# Databricks notebook source
# MAGIC %md
# MAGIC #### Explore the capablities of the dbutils.secrets.utility

# COMMAND ----------

dbutils.secrets.help()

# COMMAND ----------

dbutils.secrets.listScopes()

# COMMAND ----------

dbutils.secrets.list('formula1-scope')

# COMMAND ----------

dbutils.secrets.get(scope='formula1-scope', key='databricks-app-client-id')

# COMMAND ----------

dbutils.secrets.getBytes(scope='formula1-scope', key='databricks-app-client-id')
