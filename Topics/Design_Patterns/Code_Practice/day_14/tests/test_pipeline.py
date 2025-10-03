#tests/test_pipeline.py

from pipeline.base import DataPipeline
from pipeline.csv_pipeline import CSVPipeline
from pipeline.json_pipeline import JSONPipeline


def test_csv_pipeline(tmp_path):
    p = tmp_path / "d.csv"
    p.write_text("id,name\n1,Alice\n2,Bob\n")
    res = CSVPipeline().run(str(p))
    assert res == {"rows": 2}

def test_json_pipeline(tmp_path):
    p = tmp_path / "d.json"
    p.write_text('[{"id":1,"active":true},{"id":2,"active":false}]')
    res = JSONPipeline().run(str(p))
    assert res == {"items": 1}


