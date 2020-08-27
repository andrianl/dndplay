class Feature:
    """
    Provide full text of rules in documentation
    """
    name = "Generic Feature"
    owner = None
    source = ''  # race, class, background, etc.
    spells_known = ()
    spells_prepared = ()
    needs_implementation = False  # Set to True if need to find way to compute stats

    def weapon_func(self, *args, **kwargs):
        """
        Updates weapon based on the Feature property
        Parameters
        ----------
        weapon
           The weapon to be tested for special bonuses
        kwargs
           Any other key-word arguments the function may require
        """
        pass

    @property
    def create_feature(self, *args, **kwargs):
        """Create a new subclass of ``Feature`` with given default parameters.
        Useful for features that haven't been entered into the ``features.py``
        file yet.
        Parameters
        ----------
        params : optional
          Saved as attributes of the new class.
        Returns
        -------
        NewFeature
          New feature class, subclass of ``Feature``, with given params.
        """
        new_feature = ('UnknownFeature', (Feature,), args, kwargs)
        return new_feature
