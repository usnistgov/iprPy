# iprPy imports
from .. import Record

class PointDefectMobility(Record):
    
    @property
    def contentroot(self):
        """str: The root element of the content"""
        return 'point-defect-mobility'
    
    
    def todict(self, full=True, flat=False):
        """
        Converts the structured content to a simpler dictionary.
        
        Parameters
        ----------
        full : bool, optional
            Flag used by the calculation records.  A True value will include
            terms for both the calculation's input and results, while a value
            of False will only include input terms (Default is True).
        flat : bool, optional
            Flag affecting the format of the dictionary terms.  If True, the
            dictionary terms are limited to having only str, int, and float
            values, which is useful for comparisons.  If False, the term
            values can be of any data type, which is convenient for analysis.
            (Default is False).
            
        Returns
        -------
        dict
            A dictionary representation of the record's content.
        """
        
        ptd = self.content[self.contentroot]
        params = {}
        params['key'] = ptd['key']
        params['id'] = ptd['id']
        params['family'] = ptd['system-family']
        params['initial-defect-number'] = ptd['initial-defect-number']
        
        params['ptd_type'] = []
        params['pos'] = []
        params['atype'] = []
        params['db_vect'] = []
        params['scale'] = []
        for cp in ptd.iteraslist('calculation-parameter'):
            params['ptd_type'].append(cp.get('ptd_type', None))
            params['pos'].append(cp.get('pos', None))
            params['atype'].append(cp.get('atype', None))
            params['db_vect'].append(cp.get('db_vect', None))
            params['scale'].append(cp.get('scale', None))
        
        return params