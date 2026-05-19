import psycopg2

def get_connection():
    conn = psycopg2.connect(
        "postgresql://postgres.clsvleqivxwfiaflvcwb:shaluaolingadarius321@aws-0-eu-west-1.pooler.supabase.com:5432/postgres"
    )
    return conn

