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
from fhir.resources import measure
from fhir.resources.fhirdate import FHIRDate

from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class MeasureTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Measure", js["resourceType"])
        return measure.Measure(js)
    
    def testMeasure1(self):
        inst = self.instantiate_from("measure-composite-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Measure instance")
        self.implMeasure1(inst)
        
        js = inst.as_json()
        self.assertEqual("Measure", js["resourceType"])
        inst2 = measure.Measure(js)
        self.implMeasure1(inst2)
    
    def implMeasure1(self, inst):
        self.assertEqual(force_bytes(inst.compositeScoring.coding[0].code), force_bytes("opportunity"))
        self.assertEqual(force_bytes(inst.id), force_bytes("composite-example"))
        self.assertEqual(force_bytes(inst.relatedArtifact[0].type), force_bytes("composed-of"))
        self.assertEqual(force_bytes(inst.relatedArtifact[1].type), force_bytes("composed-of"))
        self.assertEqual(force_bytes(inst.scoring.coding[0].code), force_bytes("proportion"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Behavioral Assessment Composite Measure"))
    
    def testMeasure2(self):
        inst = self.instantiate_from("measure-component-b-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Measure instance")
        self.implMeasure2(inst)
        
        js = inst.as_json()
        self.assertEqual("Measure", js["resourceType"])
        inst2 = measure.Measure(js)
        self.implMeasure2(inst2)
    
    def implMeasure2(self, inst):
        self.assertEqual(force_bytes(inst.group[0].identifier.value), force_bytes("Main"))
        self.assertEqual(force_bytes(inst.group[0].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(force_bytes(inst.group[0].population[0].criteria), force_bytes("Initial Population"))
        self.assertEqual(force_bytes(inst.group[0].population[1].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(force_bytes(inst.group[0].population[1].criteria), force_bytes("Denominator"))
        self.assertEqual(force_bytes(inst.group[0].population[2].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(force_bytes(inst.group[0].population[2].criteria), force_bytes("Numerator"))
        self.assertEqual(force_bytes(inst.id), force_bytes("component-b-example"))
        self.assertEqual(force_bytes(inst.scoring.coding[0].code), force_bytes("proportion"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Screening for Depression"))
    
    def testMeasure3(self):
        inst = self.instantiate_from("measure-predecessor-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Measure instance")
        self.implMeasure3(inst)
        
        js = inst.as_json()
        self.assertEqual("Measure", js["resourceType"])
        inst2 = measure.Measure(js)
        self.implMeasure3(inst2)
    
    def implMeasure3(self, inst):
        self.assertEqual(inst.date.date, FHIRDate("2014-03-08").date)
        self.assertEqual(inst.date.as_json(), "2014-03-08")
        self.assertEqual(force_bytes(inst.description), force_bytes("Exclusive breastfeeding measure of outcomes for exclusive breastmilk feeding of newborns."))
        self.assertEqual(force_bytes(inst.group[0].identifier.value), force_bytes("Population Group 1"))
        self.assertEqual(force_bytes(inst.group[0].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(force_bytes(inst.group[0].population[0].criteria), force_bytes("InitialPopulation1"))
        self.assertEqual(force_bytes(inst.group[0].population[0].identifier.value), force_bytes("initial-population-1-identifier"))
        self.assertEqual(force_bytes(inst.group[0].population[1].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(force_bytes(inst.group[0].population[1].criteria), force_bytes("Denominator1"))
        self.assertEqual(force_bytes(inst.group[0].population[1].identifier.value), force_bytes("denominator-1-identifier"))
        self.assertEqual(force_bytes(inst.group[0].population[2].code.coding[0].code), force_bytes("denominator-exclusions"))
        self.assertEqual(force_bytes(inst.group[0].population[2].criteria), force_bytes("DenominatorExclusions1"))
        self.assertEqual(force_bytes(inst.group[0].population[2].identifier.value), force_bytes("denominator-exclusions-1-identifier"))
        self.assertEqual(force_bytes(inst.group[0].population[3].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(force_bytes(inst.group[0].population[3].criteria), force_bytes("Numerator1"))
        self.assertEqual(force_bytes(inst.group[0].population[3].identifier.value), force_bytes("numerator-1-identifier"))
        self.assertEqual(force_bytes(inst.group[1].identifier.value), force_bytes("Population Group 2"))
        self.assertEqual(force_bytes(inst.group[1].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(force_bytes(inst.group[1].population[0].criteria), force_bytes("InitialPopulation2"))
        self.assertEqual(force_bytes(inst.group[1].population[0].identifier.value), force_bytes("initial-population-2-identifier"))
        self.assertEqual(force_bytes(inst.group[1].population[1].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(force_bytes(inst.group[1].population[1].criteria), force_bytes("Denominator2"))
        self.assertEqual(force_bytes(inst.group[1].population[1].identifier.value), force_bytes("denominator-2-identifier"))
        self.assertEqual(force_bytes(inst.group[1].population[2].code.coding[0].code), force_bytes("denominator-exclusion"))
        self.assertEqual(force_bytes(inst.group[1].population[2].criteria), force_bytes("DenominatorExclusions2"))
        self.assertEqual(force_bytes(inst.group[1].population[2].identifier.value), force_bytes("denominator-exclusions-2-identifier"))
        self.assertEqual(force_bytes(inst.group[1].population[3].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(force_bytes(inst.group[1].population[3].criteria), force_bytes("Numerator2"))
        self.assertEqual(force_bytes(inst.group[1].population[3].identifier.value), force_bytes("numerator-2-identifier"))
        self.assertEqual(force_bytes(inst.id), force_bytes("measure-predecessor-example"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("exclusive-breastfeeding-measure"))
        self.assertEqual(force_bytes(inst.improvementNotation), force_bytes("Improvement noted as an increase in the rate"))
        self.assertEqual(force_bytes(inst.purpose), force_bytes("Measure of newborns who were fed breast milk only since birth"))
        self.assertEqual(force_bytes(inst.relatedArtifact[0].citation), force_bytes("American Academy of Pediatrics. (2005). Section on Breastfeeding. Policy Statement:Breastfeeding and the Use of Human Milk. Pediatrics.115:496-506."))
        self.assertEqual(force_bytes(inst.relatedArtifact[0].type), force_bytes("documentation"))
        self.assertEqual(force_bytes(inst.relatedArtifact[1].type), force_bytes("documentation"))
        self.assertEqual(force_bytes(inst.relatedArtifact[2].type), force_bytes("documentation"))
        self.assertEqual(force_bytes(inst.relatedArtifact[3].type), force_bytes("documentation"))
        self.assertEqual(force_bytes(inst.relatedArtifact[4].type), force_bytes("documentation"))
        self.assertEqual(force_bytes(inst.relatedArtifact[5].type), force_bytes("documentation"))
        self.assertEqual(force_bytes(inst.relatedArtifact[6].citation), force_bytes("Kramer, M.S. & Kakuma, R. (2002).Optimal duration of exclusive breastfeeding. [107 refs] Cochrane Database of Systematic Reviews. (1):CD003517."))
        self.assertEqual(force_bytes(inst.relatedArtifact[6].type), force_bytes("documentation"))
        self.assertEqual(force_bytes(inst.relatedArtifact[7].citation), force_bytes("Petrova, A., Hegyi, T., & Mehta, R. (2007). Maternal race/ethnicity and one-month exclusive breastfeeding in association with the in-hospital feeding modality. Breastfeeding Medicine. 2(2):92-8."))
        self.assertEqual(force_bytes(inst.relatedArtifact[7].type), force_bytes("documentation"))
        self.assertEqual(force_bytes(inst.relatedArtifact[8].type), force_bytes("documentation"))
        self.assertEqual(force_bytes(inst.relatedArtifact[9].type), force_bytes("documentation"))
        self.assertEqual(force_bytes(inst.scoring.coding[0].code), force_bytes("proportion"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Exclusive Breastfeeding Measure"))
        self.assertEqual(force_bytes(inst.topic[0].text), force_bytes("Exclusive Breastfeeding"))
        self.assertEqual(force_bytes(inst.type[0].coding[0].code), force_bytes("process"))
        self.assertEqual(force_bytes(inst.version), force_bytes("3.0.1"))
    
    def testMeasure4(self):
        inst = self.instantiate_from("measure-cms146-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Measure instance")
        self.implMeasure4(inst)
        
        js = inst.as_json()
        self.assertEqual("Measure", js["resourceType"])
        inst2 = measure.Measure(js)
        self.implMeasure4(inst2)
    
    def implMeasure4(self, inst):
        self.assertEqual(inst.approvalDate.date, FHIRDate("2016-01-01").date)
        self.assertEqual(inst.approvalDate.as_json(), "2016-01-01")
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].system), force_bytes("url"))
        self.assertEqual(force_bytes(inst.contact[0].telecom[0].value), force_bytes("http://www.ncqa.org/"))
        self.assertEqual(force_bytes(inst.contributor[0].name), force_bytes("National Committee for Quality Assurance"))
        self.assertEqual(force_bytes(inst.contributor[0].type), force_bytes("author"))
        self.assertEqual(inst.date.date, FHIRDate("2017-03-10").date)
        self.assertEqual(inst.date.as_json(), "2017-03-10")
        self.assertEqual(force_bytes(inst.description), force_bytes("Percentage of children 3-18 years of age who were diagnosed with pharyngitis, ordered an antibiotic and received a group A streptococcus (strep) test for the episode."))
        self.assertEqual(inst.effectivePeriod.end.date, FHIRDate("2017-12-31").date)
        self.assertEqual(inst.effectivePeriod.end.as_json(), "2017-12-31")
        self.assertEqual(inst.effectivePeriod.start.date, FHIRDate("2017-01-01").date)
        self.assertEqual(inst.effectivePeriod.start.as_json(), "2017-01-01")
        self.assertTrue(inst.experimental)
        self.assertEqual(force_bytes(inst.group[0].identifier.value), force_bytes("CMS146-group-1"))
        self.assertEqual(force_bytes(inst.group[0].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(force_bytes(inst.group[0].population[0].criteria), force_bytes("CMS146.InInitialPopulation"))
        self.assertEqual(force_bytes(inst.group[0].population[0].identifier.value), force_bytes("initial-population-identifier"))
        self.assertEqual(force_bytes(inst.group[0].population[1].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(force_bytes(inst.group[0].population[1].criteria), force_bytes("CMS146.InNumerator"))
        self.assertEqual(force_bytes(inst.group[0].population[1].identifier.value), force_bytes("numerator-identifier"))
        self.assertEqual(force_bytes(inst.group[0].population[2].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(force_bytes(inst.group[0].population[2].criteria), force_bytes("CMS146.InDenominator"))
        self.assertEqual(force_bytes(inst.group[0].population[2].identifier.value), force_bytes("denominator-identifier"))
        self.assertEqual(force_bytes(inst.group[0].population[3].code.coding[0].code), force_bytes("denominator-exclusion"))
        self.assertEqual(force_bytes(inst.group[0].population[3].criteria), force_bytes("CMS146.InDenominatorExclusions"))
        self.assertEqual(force_bytes(inst.group[0].population[3].identifier.value), force_bytes("denominator-exclusions-identifier"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].criteria), force_bytes("CMS146.AgesUpToNine"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[0].identifier.value), force_bytes("stratifier-ages-up-to-9"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].criteria), force_bytes("CMS146.AgesTenPlus"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[1].identifier.value), force_bytes("stratifier-ages-10-plus"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].identifier.value), force_bytes("stratifier-ages-up-to-9"))
        self.assertEqual(force_bytes(inst.group[0].stratifier[2].path), force_bytes("Patient.gender"))
        self.assertEqual(force_bytes(inst.guidance), force_bytes("This is an episode of care measure that examines all eligible episodes for the patient during the measurement period. If the patient has more than one episode, include all episodes in the measure"))
        self.assertEqual(force_bytes(inst.id), force_bytes("measure-cms146-example"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://hl7.org/fhir/cqi/ecqm/Measure/Identifier/cms"))
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("146"))
        self.assertEqual(force_bytes(inst.identifier[1].system), force_bytes("http://hl7.org/fhir/cqi/ecqm/Measure/Identifier/nqf"))
        self.assertEqual(force_bytes(inst.identifier[1].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.identifier[1].value), force_bytes("0002"))
        self.assertEqual(force_bytes(inst.improvementNotation), force_bytes("Higher score indicates better quality"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].code), force_bytes("US"))
        self.assertEqual(force_bytes(inst.jurisdiction[0].coding[0].system), force_bytes("urn:iso:std:iso:3166"))
        self.assertEqual(inst.lastReviewDate.date, FHIRDate("2016-09-01").date)
        self.assertEqual(inst.lastReviewDate.as_json(), "2016-09-01")
        self.assertEqual(force_bytes(inst.name), force_bytes("CMS146"))
        self.assertEqual(force_bytes(inst.publisher), force_bytes("National Committee for Quality Assurance"))
        self.assertEqual(force_bytes(inst.purpose), force_bytes("Measure of children with a group A streptococcus test in the 7-day period from 3 days prior through 3 days after the diagnosis of pharyngitis"))
        self.assertEqual(force_bytes(inst.relatedArtifact[0].citation), force_bytes("Linder, J.A., D.W. Bates, G.M. Lee, J.A. Finkelstein. 2005. \"Antibiotic treatment of children with sore throat.\" JAMA 294(18):2315-2322. "))
        self.assertEqual(force_bytes(inst.relatedArtifact[0].type), force_bytes("documentation"))
        self.assertEqual(force_bytes(inst.relatedArtifact[1].citation), force_bytes("Infectious Diseases Society of America. 2012. \"Clinical Practice Guideline for the Diagnosis and Management of Group A Streptococcal Pharyngitis: 2012 Update.\" "))
        self.assertEqual(force_bytes(inst.relatedArtifact[1].type), force_bytes("documentation"))
        self.assertEqual(force_bytes(inst.relatedArtifact[2].type), force_bytes("documentation"))
        self.assertEqual(force_bytes(inst.scoring.coding[0].code), force_bytes("proportion"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.supplementalData[0].identifier.value), force_bytes("supplemental-data-gender"))
        self.assertEqual(force_bytes(inst.supplementalData[0].path), force_bytes("Patient.gender"))
        self.assertEqual(force_bytes(inst.supplementalData[1].identifier.value), force_bytes("supplemental-data-deceased"))
        self.assertEqual(force_bytes(inst.supplementalData[1].path), force_bytes("deceasedBoolean"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("additional"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Appropriate Testing for Children with Pharyngitis"))
        self.assertEqual(force_bytes(inst.topic[0].coding[0].code), force_bytes("57024-2"))
        self.assertEqual(force_bytes(inst.topic[0].coding[0].system), force_bytes("http://hl7.org/fhir/c80-doc-typecodes"))
        self.assertEqual(force_bytes(inst.type[0].coding[0].code), force_bytes("process"))
        self.assertEqual(force_bytes(inst.url), force_bytes("http://hl7.org/fhir/Measure/measure-cms146-example"))
        self.assertEqual(force_bytes(inst.useContext[0].code.code), force_bytes("program"))
        self.assertEqual(force_bytes(inst.useContext[0].valueCodeableConcept.text), force_bytes("eligibile-provider"))
        self.assertEqual(force_bytes(inst.version), force_bytes("1.0.0"))
    
    def testMeasure5(self):
        inst = self.instantiate_from("measure-component-a-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Measure instance")
        self.implMeasure5(inst)
        
        js = inst.as_json()
        self.assertEqual("Measure", js["resourceType"])
        inst2 = measure.Measure(js)
        self.implMeasure5(inst2)
    
    def implMeasure5(self, inst):
        self.assertEqual(force_bytes(inst.group[0].identifier.value), force_bytes("Main"))
        self.assertEqual(force_bytes(inst.group[0].population[0].code.coding[0].code), force_bytes("initial-population"))
        self.assertEqual(force_bytes(inst.group[0].population[0].criteria), force_bytes("Initial Population"))
        self.assertEqual(force_bytes(inst.group[0].population[1].code.coding[0].code), force_bytes("denominator"))
        self.assertEqual(force_bytes(inst.group[0].population[1].criteria), force_bytes("Denominator"))
        self.assertEqual(force_bytes(inst.group[0].population[2].code.coding[0].code), force_bytes("numerator"))
        self.assertEqual(force_bytes(inst.group[0].population[2].criteria), force_bytes("Numerator"))
        self.assertEqual(force_bytes(inst.id), force_bytes("component-a-example"))
        self.assertEqual(force_bytes(inst.scoring.coding[0].code), force_bytes("proportion"))
        self.assertEqual(force_bytes(inst.status), force_bytes("draft"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.title), force_bytes("Screening for Alcohol Misuse"))

