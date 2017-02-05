from __future__ import print_function
import os
import shutil
import tempfile
import unittest
from StringIO import StringIO
# Import our script to test
import bm_bank_sections

# Get the current directory as the config directory for bank config file
# Add in current directory global.properties

class Test_bm_bank_sections(unittest.TestCase):
    """
    Main class to test `bm_bank_sections`
    """
    def setUp(self):
        """
        Set some info at setup
        :return:
        """
        self.current_dir = os.path.dirname(os.path.realpath(__file__))
        self.tempdir = tempfile.mkdtemp('_biomaj-scripts-tests')

        self.global_template = os.path.join(self.current_dir, 'global.properties')
        self.bank_file = os.path.join(self.current_dir, 'bank-sections.properties')
        self.manager_template = os.path.join(self.current_dir, 'manager.properties')

        for cfg_file in [self.global_template, self.bank_file, self.manager_template]:
            if not os.path.exists(cfg_file):
                raise IOError("Configuration file %s not found in %s" % (cfg_file, self.current_dir))

        self.global_properties = os.path.join(self.tempdir, 'global.properties')
        self.manager_properties = os.path.join(self.tempdir, 'manager.properties')
        self.bank_properties = os.path.join(self.tempdir, 'config', 'bank-sections.properties')
        os.makedirs(os.path.join(self.tempdir, 'config'))

        # Create new global.properties file
        fout = open(self.global_properties, 'w')
        with open(self.global_template, 'r') as fin:
            for line in fin:
                if line.startswith('root.dir'):
                    fout.write("root.dir=%s\n" % self.tempdir)
                else:
                    fout.write(line)
        fout.close()

        # Create new manager.properties file
        fout = open(self.manager_properties, 'w')
        with open(self.manager_template, 'r') as fin:
            for line in fin:
                if line.startswith('root.dir'):
                    fout.write("root.dir=%s\n" % self.tempdir)
                else:
                    fout.write(line)
        fout.close()

        # Set BIOMAJ_CONF to new test location
        os.environ['BIOMAJ_CONF'] = self.global_properties
        # Copy bank file to configdir
        shutil.copyfile(self.bank_file, self.bank_properties)

    def tearDown(self):
        shutil.rmtree(self.tempdir)

    def get_current_dir(self):
        return os.path.dirname(os.path.realpath(__file__))

    def test_argv_less_than_three_throws(self):
        """
        Check the script throws SystemExit when argv < 3
        :return:
        """
        with self.assertRaises(SystemExit):
            bm_bank_sections.main([])

    def test_tool_not_supported(self):
        """
        Check the method throws SystemExit when tool not supported
        :return:
        """
        with self.assertRaises(SystemExit):
            bm_bank_sections.main(['bank-sections', 'fake_tool'])

    def test_blast2_sections(self):
        """Check the method returns correct sections for blast2 tool"""
        saved_stout, bm_bank_sections.sys.stdout = bm_bank_sections.sys.stdout, StringIO('_')
        bm_bank_sections.main(['bank-sections', 'blast2'])
        expected = "bank_pro\nblast2_pro_sec1\nblast2_pro_sec2\nbank_nuc\nblast2_nuc_sec1\nblast2_nuc_sec2\n"
        self.assertEquals(expected, bm_bank_sections.sys.stdout.getvalue())
        bm_bank_sections.sys.stdout = saved_stout

    def test_golden_sections(self):
        """Check the method returns correct sections for golden tool"""
        saved_stout, bm_bank_sections.sys.stdout = bm_bank_sections.sys.stdout, StringIO('_')
        bm_bank_sections.main(['bank-sections', 'golden'])
        expected = "bank_pro\ngolden_pro_sec1\nbank_nuc\ngolden_nuc_sec1\n"
        self.assertEquals(expected, bm_bank_sections.sys.stdout.getvalue())
        bm_bank_sections.sys.stdout = saved_stout