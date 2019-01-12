#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.1.11917 on 2019-01-12.
#  2019, SMART Health IT.

import os
import pytest
import io
import unittest
import json
import six
from fhir.resources import conceptmap
from fhir.resources.fhirdate import FHIRDate

from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class ConceptMapTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("ConceptMap", js["resourceType"])
        return conceptmap.ConceptMap(js)
    
    def testConceptMap1(self):
        inst = self.instantiate_from("conceptmap-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ConceptMap instance")
        self.implConceptMap1(inst)
        
        js = inst.as_json()
        self.assertEqual("ConceptMap", js["resourceType"])
        inst2 = conceptmap.ConceptMap(js)
        self.implConceptMap1(inst2)
    
    def implConceptMap1(self, inst):
        self.assertEqual(force_bytes(inst.contact[0].name), force_bytes("FHIR project team (example)"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("url"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("http://hl7.org/fhir"))
        self.assertEqual(force_bytes(inst.copyright), force_bytes("Creative Commons 0"))
        self.assertEqual(inst.date.date, FHIRDate("2012-06-13").date)
        self.assertEqual(inst.date.as_json(), "2012-06-13")
        self.assertEqual(force_bytes(inst.description), force_bytes("A mapping between the FHIR and HL7 v3 AddressUse Code systems"))
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.group[0].element[0].code), force_bytes("home"))
        self.assertEqual(force_bytes(inst.group[0].element[0].display), force_bytes("home"))
        self.assertEqual(force_bytes(inst.group[0].element[0].target[0].code), force_bytes("H"))
        self.assertEqual(force_bytes(inst.group[0].element[0].target[0].display), force_bytes("home"))
        self.assertEqual(force_bytes(inst.group[0].element[1].code), force_bytes("work"))
        self.assertEqual(force_bytes(inst.group[0].element[1].display), force_bytes("work"))
        self.assertEqual(force_bytes(inst.group[0].element[1].target[0].code), force_bytes("WP"))
        self.assertEqual(force_bytes(inst.group[0].element[1].target[0].display), force_bytes("work place"))
        self.assertEqual(force_bytes(inst.group[0].element[2].code), force_bytes("temp"))
        self.assertEqual(force_bytes(inst.group[0].element[2].display), force_bytes("temp"))
        self.assertEqual(force_bytes(inst.group[0].element[2].target[0].code), force_bytes("TMP"))
        self.assertEqual(force_bytes(inst.group[0].element[2].target[0].display), force_bytes("temporary address"))
        self.assertEqual(force_bytes(inst.group[0].element[3].code), force_bytes("old"))
        self.assertEqual(force_bytes(inst.group[0].element[3].display), force_bytes("old"))
        self.assertEqual(force_bytes(inst.group[0].element[3].target[0].code), force_bytes("BAD"))
        self.assertEqual(force_bytes(inst.group[0].element[3].target[0].comment), force_bytes("In the HL7 v3 AD, old is handled by the usablePeriod element, but you have to provide a time, there's no simple equivalent of flagging an address as old"))
        self.assertEqual(force_bytes(inst.group[0].element[3].target[0].display), force_bytes("bad address"))
        self.assertEqual(force_bytes(inst.group[0].element[3].target[0].equivalence), force_bytes("disjoint"))
        self.assertEqual(force_bytes(inst.group[0].source), force_bytes("http://hl7.org/fhir/address-use"))
        self.assertEqual(force_bytes(inst.group[0].target), force_bytes("http://hl7.org/fhir/v3/AddressUse"))
        self.assertEqual(force_bytes(inst.group[0].unmapped.code), force_bytes("temp"))
        self.assertEqual(force_bytes(inst.group[0].unmapped.display), force_bytes("temp"))
        self.assertEqual(force_bytes(inst.group[0].unmapped.mode), force_bytes("fixed"))
        self.assertEqual(force_bytes(inst.id), force_bytes("101"))
        self.assertEqual(force_bytes(inst.identifier.system), force_bytes("urn:ietf:rfc:3986"))
        self.assertEqual(force_bytes(inst.identifier.value), force_bytes("urn:uuid:53cd62ee-033e-414c-9f58-3ca97b5ffc3b"))
        self.assertEqual(force_bytes(inst.name), force_bytes("FHIR-v3-Address-Use"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7, Inc"))
        self.assertEqual(force_bytes(inst.purpose), force_bytes("To help implementers map from HL7 v3/CDA to FHIR"))
        self.assertEqual(force_bytes(inst.sourceUri), force_bytes("http://hl7.org/fhir/ValueSet/address-use"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.targetUri), force_bytes("http://hl7.org/fhir/ValueSet/v3-AddressUse"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("FHIR/v3 Address Use Mapping"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://hl7.org/fhir/ConceptMap/101"))
        self.assertEqual(force_bytes(inst.useContext[0].code.code), force_bytes("venue"))
        self.assertEqual(force_bytes(inst.useContext[0].code.system), force_bytes("http://hl7.org/fhir/usage-context-type"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.text), force_bytes("for CDA Usage"))
        self.assertEqual(force_bytes(inst.version), force_bytes("20120613"))
    
    def testConceptMap2(self):
        inst = self.instantiate_from("conceptmap-example-2.json")
        self.assertIsNotNone(inst, "Must have instantiated a ConceptMap instance")
        self.implConceptMap2(inst)
        
        js = inst.as_json()
        self.assertEqual("ConceptMap", js["resourceType"])
        inst2 = conceptmap.ConceptMap(js)
        self.implConceptMap2(inst2)
    
    def implConceptMap2(self, inst):
        self.assertEqual(force_bytes(inst.contact[0].name), force_bytes("FHIR project team (example)"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("url"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("http://hl7.org/fhir"))
        self.assertEqual(inst.date.date, FHIRDate("2012-06-13").date)
        self.assertEqual(inst.date.as_json(), "2012-06-13")
        self.assertEqual(force_bytes(inst.description), force_bytes("An example mapping"))
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.group[0].element[0].code), force_bytes("code"))
        self.assertEqual(force_bytes(inst.group[0].element[0].display), force_bytes("Example Code"))
        self.assertEqual(force_bytes(inst.group[0].element[0].target[0].code), force_bytes("code2"))
        self.assertEqual(force_bytes(inst.group[0].element[0].target[0].dependsOn[0].code), force_bytes("some-code"))
        self.assertEqual(force_bytes(inst.group[0].element[0].target[0].dependsOn[0].display), force_bytes("Something Coded"))
        self.assertEqual(force_bytes(inst.group[0].element[0].target[0].dependsOn[0].property), force_bytes("http://example.org/fhir/DataElement/example"))
        self.assertEqual(force_bytes(inst.group[0].element[0].target[0].dependsOn[0].system), force_bytes("http://example.org/fhir/example3"))
        self.assertEqual(force_bytes(inst.group[0].element[0].target[0].display), force_bytes("Some Example Code"))
        self.assertEqual(force_bytes(inst.group[0].element[0].target[0].equivalence), force_bytes("equivalent"))
        self.assertEqual(force_bytes(inst.group[0].source), force_bytes("http://example.org/fhir/example1"))
        self.assertEqual(force_bytes(inst.group[0].target), force_bytes("http://example.org/fhir/example2"))
        self.assertEqual(force_bytes(inst.group[0].unmapped.mode), force_bytes("other-map"))
        self.assertEqual(force_bytes(inst.group[0].unmapped.url), force_bytes("http://example.org/fhir/ConceptMap/map2"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example2"))
        self.assertEqual(force_bytes(inst.name), force_bytes("FHIR-exanple-2"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("HL7, Inc"))
        self.assertEqual(force_bytes(inst.purpose), force_bytes("To illustrate mapping features"))
        self.assertEqual(force_bytes(inst.sourceUri), force_bytes("http://example.org/fhir/example1"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.targetUri), force_bytes("http://example.org/fhir/example2"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("FHIR Example 2"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://hl7.org/fhir/ConceptMap/example2"))
    
    def testConceptMap3(self):
        inst = self.instantiate_from("conceptmap-example-specimen-type.json")
        self.assertIsNotNone(inst, "Must have instantiated a ConceptMap instance")
        self.implConceptMap3(inst)
        
        js = inst.as_json()
        self.assertEqual("ConceptMap", js["resourceType"])
        inst2 = conceptmap.ConceptMap(js)
        self.implConceptMap3(inst2)
    
    def implConceptMap3(self, inst):
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("url"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("http://hl7.org/fhir"))
        self.assertEqual(force_bytes(inst.contact[1].telecom[0].system), force_bytes("url"))
        self.assertEqual(force_bytes(inst.contact[1].telecom[0].value), force_bytes("http://www.phconnect.org/group/laboratorymessagingcommunityofpractice/forum/attachment/download?id=3649725%3AUploadedFile%3A145786"))
        self.assertEqual(inst.date.date, FHIRDate("2013-07-25").date)
        self.assertEqual(inst.date.as_json(), "2013-07-25")
        self.assertFalse(inst.experimental)
        self.assertEqual(force_bytes(inst.group[0].element[0].code), force_bytes("ACNE"))
        self.assertEqual(force_bytes(inst.group[0].element[0].target[0].code), force_bytes("309068002"))
        self.assertEqual(force_bytes(inst.group[0].element[1].code), force_bytes("ACNFLD"))
        self.assertEqual(force_bytes(inst.group[0].element[1].target[0].code), force_bytes("119323008"))
        self.assertEqual(force_bytes(inst.group[0].element[1].target[0].comment), force_bytes("HL7 term is a historical term. mapped to Pus"))
        self.assertEqual(force_bytes(inst.group[0].element[1].target[0].product[0].code), force_bytes("47002008"))
        self.assertEqual(force_bytes(inst.group[0].element[1].target[0].product[0].property), force_bytes("TypeModifier"))
        self.assertEqual(force_bytes(inst.group[0].element[1].target[0].product[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.group[0].element[2].code), force_bytes("AIRS"))
        self.assertEqual(force_bytes(inst.group[0].element[2].target[0].code), force_bytes("446302006"))
        self.assertEqual(force_bytes(inst.group[0].element[3].code), force_bytes("ALL"))
        self.assertEqual(force_bytes(inst.group[0].element[3].target[0].code), force_bytes("119376003"))
        self.assertEqual(force_bytes(inst.group[0].element[3].target[0].product[0].code), force_bytes("7970006"))
        self.assertEqual(force_bytes(inst.group[0].element[3].target[0].product[0].property), force_bytes("TypeModifier"))
        self.assertEqual(force_bytes(inst.group[0].element[3].target[0].product[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.group[0].element[4].code), force_bytes("AMP"))
        self.assertEqual(force_bytes(inst.group[0].element[4].target[0].code), force_bytes("408654003"))
        self.assertEqual(force_bytes(inst.group[0].element[4].target[0].product[0].code), force_bytes("81723002"))
        self.assertEqual(force_bytes(inst.group[0].element[4].target[0].product[0].property), force_bytes("http://snomed.info/id/246380002"))
        self.assertEqual(force_bytes(inst.group[0].element[4].target[0].product[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.group[0].element[5].code), force_bytes("ANGI"))
        self.assertEqual(force_bytes(inst.group[0].element[5].target[0].code), force_bytes("119312009"))
        self.assertEqual(force_bytes(inst.group[0].element[5].target[0].comment), force_bytes("TBD in detail"))
        self.assertEqual(force_bytes(inst.group[0].element[6].code), force_bytes("ARTC"))
        self.assertEqual(force_bytes(inst.group[0].element[6].target[0].code), force_bytes("119312009"))
        self.assertEqual(force_bytes(inst.group[0].element[6].target[0].comment), force_bytes("TBD in detail"))
        self.assertEqual(force_bytes(inst.group[0].element[7].code), force_bytes("ASERU"))
        self.assertEqual(force_bytes(inst.group[0].element[7].target[0].comment), force_bytes("pending"))
        self.assertEqual(force_bytes(inst.group[0].element[7].target[0].equivalence), force_bytes("unmatched"))
        self.assertEqual(force_bytes(inst.group[0].element[8].code), force_bytes("ASP"))
        self.assertEqual(force_bytes(inst.group[0].element[8].target[0].code), force_bytes("119295008"))
        self.assertEqual(force_bytes(inst.group[0].element[8].target[0].product[0].code), force_bytes("14766002"))
        self.assertEqual(force_bytes(inst.group[0].element[8].target[0].product[0].property), force_bytes("http://snomed.info/id/246380002"))
        self.assertEqual(force_bytes(inst.group[0].element[8].target[0].product[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.group[0].element[9].code), force_bytes("ATTE"))
        self.assertEqual(force_bytes(inst.group[0].element[9].target[0].comment), force_bytes("TBD"))
        self.assertEqual(force_bytes(inst.group[0].element[9].target[0].equivalence), force_bytes("unmatched"))
        self.assertEqual(force_bytes(inst.group[0].source), force_bytes("http://hl7.org/fhir/v2/0487"))
        self.assertEqual(force_bytes(inst.group[0].target), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.id), force_bytes("102"))
        self.assertEqual(force_bytes(inst.name), force_bytes("Specimen mapping from v2 table 0487 to SNOMED CT"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("FHIR project team (original source: LabMCoP)"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://hl7.org/fhir/ConceptMap/102"))
        self.assertEqual(force_bytes(inst.version), force_bytes("20130725"))

