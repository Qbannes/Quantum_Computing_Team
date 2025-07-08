```
token = "dein token"

QiskitRuntimeService.save_account(
    channel="ibm_cloud",         
    token=token,
    instance="Projekt Zufall 1",  # Instanzname
    overwrite=True,
    set_as_default=True
)
```
Verweis auf Konto mithilfe von API-Token
Verweis auf Instanz
Wird als Standard gesetzt
```
from qiskit_ibm_runtime import SamplerV2 as Sampler

backend_name = service.backend(name = 'ibm_brisbane')

sampler = Sampler(mode=backend_name)
job = sampler.run([isa_circuit], shots = 1000)

print("Job-ID:", job.job_id())
```
Sampler, um Werte zu erhalten und nicht das Andere (mit Estimator).
service = QiskitRuntimeService() verweist automatisch auf die vorher gespeicherten Daten.