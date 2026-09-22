# system-simulation

Executable learning models for understanding systems.

First vertical slice:

- **Subject:** Finance
- **Chapter 01:** Claims and balance sheets
- **Learning goal:** understand that one financial claim is simultaneously an asset of its holder and a liability of its issuer.
- **Model:** create, transfer, and settle a claim.
- **Observation:** every scenario step produces an explicit before/after trace.

## Run the CLI demo

No package installation is required:

```powershell
python .\run_demo.py
```

## Run tests

```powershell
python -m unittest discover -s tests -v
```

## Run the Streamlit UI

```powershell
pip install -r .\requirements-ui.txt
streamlit run .\apps\streamlit_app.py
```

The UI is intentionally a thin observer over the model. It does not contain domain rules.

## Optional editable install

For development, the source package can also be installed in editable mode:

```powershell
pip install -e .
```
