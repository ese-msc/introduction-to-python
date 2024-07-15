import pybryt
import pathlib


def pybryt_reference(lecture, exercise):
    """Function for obtaining the ``.pkl`` PyBryt reference.

    If ``.py`` reference is present, it is compiled (and existing ``.pkl``
    reference overwritten). Otherwise, an existing ``.pkl`` file is returned.

    Parameters
    ----------
    lecture: int

        Lecture number.

    exercise: int

        Exercise number.

    Returns
    -------
    pathlib.Path

        ``.pkl`` file path.

    Raises
    ------
    FileNotFoundError

        Neither ``.py`` nor ``.pkl`` files exist.

    """
    dirname = pathlib.Path("pybryt-references")
    basename = f"exercise-{lecture}_{exercise}"
    pyfilename = dirname / f"{basename}.py"
    pklfilename = dirname / f"{basename}.pkl"

    if pyfilename.is_file():
        pybryt.ReferenceImplementation.compile(str(pyfilename)).dump(str(pklfilename))
    elif not pklfilename.is_file():
        msg = f"PyBryt reference {pklfilename!r} not found."
        raise FileNotFoundError(msg)

    return str(pklfilename)
