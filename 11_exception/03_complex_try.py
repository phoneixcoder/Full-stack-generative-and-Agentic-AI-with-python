def serve_chai(flavor):
    try:
        print (f"Preparing {flavor} chai...")
        if flavor == "unknown":
            raise ValueError("We don't know what flavor you want")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print("Preparation complete")
    finally:
        print("Next customer please")

serve_chai("milk")
serve_chai("unknown")