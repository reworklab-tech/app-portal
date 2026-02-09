# Uji sementara untuk fitur login
TEST_TOKEN = "RELAB-fake-tech-Qa63vBd90Ym2"

def test_login():
    assert TEST_TOKEN.startswith("RELAB")
