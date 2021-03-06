# Copyright (C) 2010-2014 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

import os

from lib.cuckoo.common.abstracts import Processing
from lib.cuckoo.common.objects import File
from lib.cuckoo.common.constants import CUCKOO_ROOT

class ProcessMemory(Processing):
    """Analyze process memory dumps."""

    def run(self):
        """Run analysis.
        @return: structured results.
        """
        self.key = "procmemory"
        results = []

        for dmp in os.listdir(self.pmemory_path):
            dmp_path = os.path.join(self.pmemory_path, dmp)
            dmp_file = File(dmp_path)

            proc = dict(
                yara=dmp_file.get_yara(os.path.join(CUCKOO_ROOT, "data", "yara", "index_memory.yar"))
            )

            results.append(proc)

        return results
