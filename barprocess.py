import time
from tqdm.rich import tqdm


class barprocess:
    """
    class to create progress bar
    """
    def __init__(self):
        for _ in tqdm(
            range(30),
            desc="Procesando",
            bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}",
            ncols=60,
        ):
            time.sleep(0.05)  # Simula actividad
