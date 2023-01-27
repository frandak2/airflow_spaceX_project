from airflow.models import BaseOperator
import pandas as pd

class GeneratesatelliteDataOperator(BaseOperator):
    template_fields = ('logical_date', 'ds_nodash')
    def __init__(self, logical_date, ds_nodash, *args, **kwargs):
        self.logical_date = logical_date
        self.ds_nodash = ds_nodash
        super().__init__(*args, **kwargs)

    def execute(self, context):
        def _generate_platzi_data():
            print(f"La fecha lógica es: {self.logical_date}")
            data = pd.DataFrame({"student": ["Maria Cruz", "Daniel Crema",
                                            "Elon Musk", "Karol Castrejon", "Freddy Vega"],
                                "timestamp": [self.logical_date, self.logical_date, self.logical_date, self.logical_date, self.logical_date]})
            data.to_csv(f"/tmp/platzi_data_{self.ds_nodash}.csv", header=True)
            print(f"archivo creado en: /tmp/platzi_data_{self.ds_nodash}.csv")
        _generate_platzi_data()





