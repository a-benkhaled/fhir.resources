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
from fhir.resources import structuredefinition
from fhir.resources.fhirdate import FHIRDate

from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class StructureDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("StructureDefinition", js["resourceType"])
        return structuredefinition.StructureDefinition(js)
    
    def testStructureDefinition1(self):
        inst = self.instantiate_from("structuredefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a StructureDefinition instance")
        self.implStructureDefinition1(inst)
        
        js = inst.as_json()
        self.assertEqual("StructureDefinition", js["resourceType"])
        inst2 = structuredefinition.StructureDefinition(js)
        self.implStructureDefinition1(inst2)
    
    def implStructureDefinition1(self, inst):
        self.assertFalse(inst.abstract)
        self.assertEqual(force_bytes(inst.baseDefinition), force_bytes("http://hl7.org/fhir/StructureDefinition/DiagnosticReport"))
        self.assertEqual(force_bytes(inst.contact[0].name), force_bytes("Grahame Grieve"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("email"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("grahame@healthintersections.com.au"))
        self.assertEqual(force_bytes(inst.copyright), force_bytes("Creative Commons 0, per FHIR specification"))
        self.assertEqual(inst.date.date, FHIRDate("2012-05-12").date)
        self.assertEqual(inst.date.as_json(), "2012-05-12")
        self.assertEqual(force_bytes(inst.derivation), force_bytes("constraint"))
        self.assertEqual(force_bytes(inst.description), force_bytes("Describes how the lab report is used for a standard Lipid Profile - Cholesterol, Triglyceride and Cholesterol fractions. Uses LOINC codes"))
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.fhirVersion), force_bytes("1.0.0"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("1.2.36.90146595217.4.2"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("AU"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].system), force_bytes("urn:iso:std:iso:3166"))
        self.assertEqual(force_bytes(inst.keyword[0].code), force_bytes("314079002"))
        self.assertEqual(force_bytes(inst.keyword[0].display), force_bytes("Hyperlipidemia screening test (procedure)"))
        self.assertEqual(force_bytes(inst.keyword[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.kind), force_bytes("resource"))
        self.assertEqual(force_bytes(inst.mapping[0].comment), force_bytes("Actual mappings haven't yet been filled out"))
        self.assertEqual(force_bytes(inst.mapping[0].identity), force_bytes("m1"))
        self.assertEqual(force_bytes(inst.mapping[0].name), force_bytes("RCPA Lipid Report recommendations"))
        self.assertEqual(force_bytes(inst.mapping[0].uri), force_bytes("https://www.rcpa.edu.au/getattachment/0961c6d1-ec80-4500-8dc0-de516500e05b/Lipid-and-lipoprotein-testing.aspx"))
        self.assertEqual(force_bytes(inst.name), force_bytes("LipidProfileExample"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("Health Intersections Pty Ltd"))
        self.assertEqual(force_bytes(inst.purpose), force_bytes("Provide an example to demonstrate how to use StructureDefinition"))
        self.assertEqual(force_bytes(inst.snapshot.element[0].base.max), force_bytes("1"))
        self.assertEqual(inst.snapshot.element[0].base.min, 1)
        self.assertEqual(force_bytes(inst.snapshot.element[0].base.path), force_bytes("DiagnosticReport"))
        self.assertEqual(force_bytes(inst.snapshot.element[0].definition), force_bytes("The findings and interpretation of a general lipd lab profile."))
        self.assertEqual(force_bytes(inst.snapshot.element[0].id), force_bytes("DiagnosticReport"))
        self.assertFalse(inst.snapshot.element[0].isModifier)
        self.assertEqual(force_bytes(inst.snapshot.element[0].max), force_bytes("1"))
        self.assertEqual(inst.snapshot.element[0].min, 1)
        self.assertEqual(force_bytes(inst.snapshot.element[0].path), force_bytes("DiagnosticReport"))
        self.assertEqual(force_bytes(inst.snapshot.element[0].short), force_bytes("Lipid Lab Report"))
        self.assertEqual(force_bytes(inst.snapshot.element[1].base.max), force_bytes("*"))
        self.assertEqual(inst.snapshot.element[1].base.min, 0)
        self.assertEqual(force_bytes(inst.snapshot.element[1].base.path), force_bytes("DiagnosticReport.extension"))
        self.assertEqual(force_bytes(inst.snapshot.element[1].id), force_bytes("DiagnosticReport.extension"))
        self.assertFalse(inst.snapshot.element[1].isModifier)
        self.assertEqual(force_bytes(inst.snapshot.element[1].max), force_bytes("*"))
        self.assertEqual(inst.snapshot.element[1].min, 0)
        self.assertEqual(force_bytes(inst.snapshot.element[1].path), force_bytes("DiagnosticReport.extension"))
        self.assertEqual(force_bytes(inst.snapshot.element[1].short), force_bytes("Additional Content defined by implementations"))
        self.assertEqual(force_bytes(inst.snapshot.element[1].slicing.discriminator[0].path), force_bytes("url"))
        self.assertEqual(force_bytes(inst.snapshot.element[1].slicing.discriminator[0].type), force_bytes("value"))
        self.assertFalse(inst.snapshot.element[1].slicing.ordered)
        self.assertEqual(force_bytes(inst.snapshot.element[1].slicing.rules), force_bytes("open"))
        self.assertEqual(force_bytes(inst.snapshot.element[1].type[0].code), force_bytes("Extension"))
        self.assertEqual(force_bytes(inst.snapshot.element[2].alias[0]), force_bytes("narrative"))
        self.assertEqual(force_bytes(inst.snapshot.element[2].alias[1]), force_bytes("html"))
        self.assertEqual(force_bytes(inst.snapshot.element[2].alias[2]), force_bytes("xhtml"))
        self.assertEqual(force_bytes(inst.snapshot.element[2].alias[3]), force_bytes("display"))
        self.assertEqual(force_bytes(inst.snapshot.element[2].base.max), force_bytes("1"))
        self.assertEqual(inst.snapshot.element[2].base.min, 0)
        self.assertEqual(force_bytes(inst.snapshot.element[2].base.path), force_bytes("DiagnosticReport.text"))
        self.assertEqual(force_bytes(inst.snapshot.element[2].comment), force_bytes("Contained resources do not have narrative. Resources that are not contained SHOULD have a narrative."))
        self.assertEqual(force_bytes(inst.snapshot.element[2].id), force_bytes("DiagnosticReport.text"))
        self.assertFalse(inst.snapshot.element[2].isModifier)
        self.assertEqual(force_bytes(inst.snapshot.element[2].max), force_bytes("1"))
        self.assertEqual(inst.snapshot.element[2].min, 0)
        self.assertEqual(force_bytes(inst.snapshot.element[2].path), force_bytes("DiagnosticReport.text"))
        self.assertEqual(force_bytes(inst.snapshot.element[2].short), force_bytes("Text summary of the resource, for human interpretation"))
        self.assertEqual(force_bytes(inst.snapshot.element[2].type[0].code), force_bytes("Narrative"))
        self.assertEqual(force_bytes(inst.snapshot.element[3].alias[0]), force_bytes("inline resources"))
        self.assertEqual(force_bytes(inst.snapshot.element[3].alias[1]), force_bytes("anonymous resources"))
        self.assertEqual(force_bytes(inst.snapshot.element[3].alias[2]), force_bytes("contained resources"))
        self.assertEqual(force_bytes(inst.snapshot.element[3].base.max), force_bytes("*"))
        self.assertEqual(inst.snapshot.element[3].base.min, 0)
        self.assertEqual(force_bytes(inst.snapshot.element[3].base.path), force_bytes("DiagnosticReport.contained"))
        self.assertEqual(force_bytes(inst.snapshot.element[3].comment), force_bytes("This should never be done when the content can be identified properly, as once identification is lost, it is extremely difficult (and context dependent) to restore it again."))
        self.assertEqual(force_bytes(inst.snapshot.element[3].id), force_bytes("DiagnosticReport.contained"))
        self.assertFalse(inst.snapshot.element[3].isModifier)
        self.assertEqual(force_bytes(inst.snapshot.element[3].max), force_bytes("*"))
        self.assertEqual(inst.snapshot.element[3].min, 0)
        self.assertEqual(force_bytes(inst.snapshot.element[3].path), force_bytes("DiagnosticReport.contained"))
        self.assertEqual(force_bytes(inst.snapshot.element[3].short), force_bytes("Contained, inline Resources"))
        self.assertEqual(force_bytes(inst.snapshot.element[3].type[0].code), force_bytes("Resource"))
        self.assertEqual(force_bytes(inst.snapshot.element[4].base.max), force_bytes("1"))
        self.assertEqual(inst.snapshot.element[4].base.min, 1)
        self.assertEqual(force_bytes(inst.snapshot.element[4].base.path), force_bytes("DiagnosticReport.status"))
        self.assertEqual(force_bytes(inst.snapshot.element[4].binding.strength), force_bytes("required"))
        self.assertEqual(force_bytes(inst.snapshot.element[4].comment), force_bytes("This is labeled as \"Is Modifier\" because applications need to take appropriate action if a report is withdrawn."))
        self.assertEqual(force_bytes(inst.snapshot.element[4].definition), force_bytes("The status of the diagnostic report as a whole."))
        self.assertEqual(force_bytes(inst.snapshot.element[4].id), force_bytes("DiagnosticReport.status"))
        self.assertFalse(inst.snapshot.element[4].isModifier)
        self.assertEqual(force_bytes(inst.snapshot.element[4].max), force_bytes("1"))
        self.assertEqual(inst.snapshot.element[4].min, 1)
        self.assertEqual(force_bytes(inst.snapshot.element[4].path), force_bytes("DiagnosticReport.status"))
        self.assertEqual(force_bytes(inst.snapshot.element[4].short), force_bytes("registered|interim|final|amended|cancelled|withdrawn"))
        self.assertEqual(force_bytes(inst.snapshot.element[4].type[0].code), force_bytes("code"))
        self.assertEqual(force_bytes(inst.snapshot.element[5].base.max), force_bytes("1"))
        self.assertEqual(inst.snapshot.element[5].base.min, 1)
        self.assertEqual(force_bytes(inst.snapshot.element[5].base.path), force_bytes("DiagnosticReport.issued"))
        self.assertEqual(force_bytes(inst.snapshot.element[5].comment), force_bytes("May be different from the update time of the resource itself, because that is the status of the record (potentially a secondary copy), not the actual release time of the report."))
        self.assertEqual(force_bytes(inst.snapshot.element[5].definition), force_bytes("The date and/or time that this version of the report was released from the source diagnostic service."))
        self.assertEqual(force_bytes(inst.snapshot.element[5].id), force_bytes("DiagnosticReport.issued"))
        self.assertFalse(inst.snapshot.element[5].isModifier)
        self.assertEqual(force_bytes(inst.snapshot.element[5].max), force_bytes("1"))
        self.assertEqual(inst.snapshot.element[5].min, 1)
        self.assertEqual(force_bytes(inst.snapshot.element[5].path), force_bytes("DiagnosticReport.issued"))
        self.assertEqual(force_bytes(inst.snapshot.element[5].short), force_bytes("Date this version was released"))
        self.assertEqual(force_bytes(inst.snapshot.element[5].type[0].code), force_bytes("dateTime"))
        self.assertEqual(force_bytes(inst.snapshot.element[6].base.max), force_bytes("1"))
        self.assertEqual(inst.snapshot.element[6].base.min, 1)
        self.assertEqual(force_bytes(inst.snapshot.element[6].base.path), force_bytes("DiagnosticReport.subject"))
        self.assertEqual(force_bytes(inst.snapshot.element[6].definition), force_bytes("The subject of the report. Usually, but not always, this is a patient. However diagnostic services also perform analyses on specimens collected from a variety of other sources."))
        self.assertEqual(force_bytes(inst.snapshot.element[6].id), force_bytes("DiagnosticReport.subject"))
        self.assertFalse(inst.snapshot.element[6].isModifier)
        self.assertEqual(force_bytes(inst.snapshot.element[6].max), force_bytes("1"))
        self.assertEqual(inst.snapshot.element[6].min, 1)
        self.assertEqual(force_bytes(inst.snapshot.element[6].path), force_bytes("DiagnosticReport.subject"))
        self.assertEqual(force_bytes(inst.snapshot.element[6].short), force_bytes("The subject of the report"))
        self.assertEqual(force_bytes(inst.snapshot.element[6].type[0].aggregation[0]), force_bytes("bundled"))
        self.assertEqual(force_bytes(inst.snapshot.element[6].type[0].code), force_bytes("Reference"))
        self.assertEqual(force_bytes(inst.snapshot.element[6].type[0].targetProfile), force_bytes("http://hl7.org/fhir/StructureDefinition/Patient"))
        self.assertEqual(force_bytes(inst.snapshot.element[6].type[0].versioning), force_bytes("either"))
        self.assertEqual(force_bytes(inst.snapshot.element[6].type[1].aggregation[0]), force_bytes("bundled"))
        self.assertEqual(force_bytes(inst.snapshot.element[6].type[1].code), force_bytes("Reference"))
        self.assertEqual(force_bytes(inst.snapshot.element[6].type[1].targetProfile), force_bytes("http://hl7.org/fhir/StructureDefinition/Group"))
        self.assertEqual(force_bytes(inst.snapshot.element[6].type[2].aggregation[0]), force_bytes("bundled"))
        self.assertEqual(force_bytes(inst.snapshot.element[6].type[2].code), force_bytes("Reference"))
        self.assertEqual(force_bytes(inst.snapshot.element[6].type[2].targetProfile), force_bytes("http://hl7.org/fhir/StructureDefinition/Device"))
        self.assertEqual(force_bytes(inst.snapshot.element[7].base.max), force_bytes("1"))
        self.assertEqual(inst.snapshot.element[7].base.min, 1)
        self.assertEqual(force_bytes(inst.snapshot.element[7].base.path), force_bytes("DiagnosticReport.performer"))
        self.assertEqual(force_bytes(inst.snapshot.element[7].comment), force_bytes("This is not necessarily the source of the atomic data items - it's the entity that takes responsibility for the clinical report."))
        self.assertEqual(force_bytes(inst.snapshot.element[7].definition), force_bytes("The diagnostic service that is responsible for issuing the report."))
        self.assertEqual(force_bytes(inst.snapshot.element[7].id), force_bytes("DiagnosticReport.performer"))
        self.assertFalse(inst.snapshot.element[7].isModifier)
        self.assertEqual(force_bytes(inst.snapshot.element[7].max), force_bytes("1"))
        self.assertEqual(inst.snapshot.element[7].min, 1)
        self.assertEqual(force_bytes(inst.snapshot.element[7].path), force_bytes("DiagnosticReport.performer"))
        self.assertEqual(force_bytes(inst.snapshot.element[7].short), force_bytes("Responsible Diagnostic Service"))
        self.assertEqual(force_bytes(inst.snapshot.element[7].type[0].code), force_bytes("Reference"))
        self.assertEqual(force_bytes(inst.snapshot.element[7].type[0].targetProfile), force_bytes("http://hl7.org/fhir/StructureDefinition/Organization"))
        self.assertEqual(force_bytes(inst.snapshot.element[8].base.max), force_bytes("*"))
        self.assertEqual(inst.snapshot.element[8].base.min, 0)
        self.assertEqual(force_bytes(inst.snapshot.element[8].base.path), force_bytes("DiagnosticReport.identifier"))
        self.assertEqual(force_bytes(inst.snapshot.element[8].definition), force_bytes("The local ID assigned to the report by the order filler, usually by the Information System of the diagnostic service provider."))
        self.assertEqual(force_bytes(inst.snapshot.element[8].id), force_bytes("DiagnosticReport.identifier"))
        self.assertFalse(inst.snapshot.element[8].isModifier)
        self.assertEqual(force_bytes(inst.snapshot.element[8].max), force_bytes("1"))
        self.assertEqual(inst.snapshot.element[8].min, 0)
        self.assertEqual(force_bytes(inst.snapshot.element[8].path), force_bytes("DiagnosticReport.identifier"))
        self.assertEqual(force_bytes(inst.snapshot.element[8].short), force_bytes("Id for external references to this report"))
        self.assertEqual(force_bytes(inst.snapshot.element[8].type[0].code), force_bytes("Identifier"))
        self.assertEqual(force_bytes(inst.snapshot.element[9].base.max), force_bytes("*"))
        self.assertEqual(inst.snapshot.element[9].base.min, 0)
        self.assertEqual(force_bytes(inst.snapshot.element[9].base.path), force_bytes("DiagnosticReport.request"))
        self.assertEqual(force_bytes(inst.snapshot.element[9].definition), force_bytes("Details concerning a single pathology test requested."))
        self.assertEqual(force_bytes(inst.snapshot.element[9].id), force_bytes("DiagnosticReport.request"))
        self.assertFalse(inst.snapshot.element[9].isModifier)
        self.assertEqual(force_bytes(inst.snapshot.element[9].max), force_bytes("*"))
        self.assertEqual(inst.snapshot.element[9].min, 0)
        self.assertEqual(force_bytes(inst.snapshot.element[9].path), force_bytes("DiagnosticReport.request"))
        self.assertEqual(force_bytes(inst.snapshot.element[9].short), force_bytes("What was requested"))
        self.assertEqual(force_bytes(inst.snapshot.element[9].type[0].aggregation[0]), force_bytes("referenced"))
        self.assertEqual(force_bytes(inst.snapshot.element[9].type[0].code), force_bytes("Reference"))
        self.assertEqual(force_bytes(inst.snapshot.element[9].type[0].targetProfile), force_bytes("http://hl7.org/fhir/StructureDefinition/ProcedureRequest"))
        self.assertEqual(force_bytes(inst.snapshot.element[9].type[0].versioning), force_bytes("specific"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Example Lipid Profile"))
        self.assertEqual(force_bytes(inst.type), force_bytes("DiagnosticReport"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://hl7.org/fhir/StructureDefinition/example"))
        self.assertEqual(force_bytes(inst.useContext[0].code.code), force_bytes("focus"))
        self.assertEqual(force_bytes(inst.useContext[0].code.display), force_bytes("Clinical Focus"))
        self.assertEqual(force_bytes(inst.useContext[0].code.system), force_bytes("http://hl7.org/fhir/usage-context-type"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].code), force_bytes("314079002"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].display), force_bytes("Hyperlipidemia screening test (procedure)"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.version), force_bytes("2"))

