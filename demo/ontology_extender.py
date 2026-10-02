"""
Secondary Ontology Completeness Extender & Description Logic Subsumption Engine.

Generates complete RDF/OWL/JSON-LD knowledge graphs, executes Description Logic (DL)
subsumption reasoning via prolog_engine, and computes mathematical Ontology Completeness metrics.
"""

import json
import math
from typing import Dict, List, Any, Set
from demo.gnosis import GnosisExtractor
from demo.cut_up_engine import CutUpEngine
from demo.prolog_engine import DescriptionLogicReasoner

class SecondaryOntologyExtender:
    def __init__(self):
        self.gnosis = GnosisExtractor()
        self.cut_up = CutUpEngine()
        self.reasoner = DescriptionLogicReasoner()

    def deconstruct_primary_ontology(self, primary_text: str, counter_text: str) -> Dict[str, Any]:
        """
        Collides primary text with counter-narrative text to surface hidden entities,
        redefine existing entities, discover new subversive relationships,
        and perform DL subsumption proofs.
        """
        recombined = self.cut_up.fold_in(primary_text, counter_text)
        analysis = self.gnosis.analyze_cut_up(recombined)

        primary_terms = self.gnosis.extract_keywords(primary_text, top_n=5)
        counter_terms = self.gnosis.extract_keywords(counter_text, top_n=5)

        # DL Axiom Setup in Prolog Reasoner
        self.reasoner.add_subclass("PrimaryControlEntity", "SystemicDominance")
        self.reasoner.add_subclass("SecondaryCriticalEntity", "LiberatoryCounterConcept")

        entities = []
        for term, cnt in primary_terms:
            ent_id = f"Primary_{term.capitalize()}"
            entities.append({
                "@id": f"ontology:{ent_id}",
                "@type": "PrimaryControlEntity",
                "label": term,
                "status": "TargetOfDeconstruction",
                "critique": "Embodiment of dominant control grammar."
            })
            self.reasoner.add_instance(ent_id, "PrimaryControlEntity")

        for term, cnt in counter_terms:
            ent_id = f"Secondary_{term.capitalize()}"
            entities.append({
                "@id": f"ontology:{ent_id}",
                "@type": "SecondaryCriticalEntity",
                "label": term,
                "status": "LiberatoryCounterConcept",
                "role": "Interferes with primary ontology repetition."
            })
            self.reasoner.add_instance(ent_id, "SecondaryCriticalEntity")

        # Verify DL Subsumption: Is PrimaryControlEntity subsumed by SystemicDominance?
        dl_proof = self.reasoner.is_subsumed_by("PrimaryControlEntity", "SystemicDominance")

        relationships = []
        for w1, w2 in analysis["juxtaposition_pairs"]:
            relationships.append({
                "subject": f"ontology:{w1.capitalize()}",
                "predicate": "subverts_or_exposes",
                "object": f"ontology:{w2.capitalize()}",
                "context": "Emergent relationship from fold-in juxtaposition."
            })

        axioms = [
            r"Axiom 1: PrimaryControlEntity \sqsubseteq SystemicDominance",
            r"Axiom 2: SecondaryCriticalEntity \sqsubseteq LiberatoryCounterConcept",
            r"Axiom 3: \forall x. SubvertsOrExposes(x) \implies DisruptionOfWordLines(x)"
        ]

        # Calculate Formal Ontology Completeness Metrics
        num_entities = len(entities)
        num_rels = len(relationships)
        num_axioms = len(axioms)
        completeness_score = round(min(1.0, (num_entities * 0.4 + num_rels * 0.4 + num_axioms * 0.2) / 10.0), 4)

        json_ld = {
            "@context": {
                "ontology": "http://burroughs.machine/schema/v2#",
                "PrimaryControlEntity": "ontology:PrimaryControlEntity",
                "SecondaryCriticalEntity": "ontology:SecondaryCriticalEntity",
                "subverts_or_exposes": "ontology:subverts_or_exposes"
            },
            "@graph": entities,
            "relationships": relationships,
            "dl_axioms": axioms,
            "dl_subsumption_proof_valid": dl_proof,
            "completeness_metrics": {
                "entity_count": num_entities,
                "relationship_count": num_rels,
                "dl_axiom_count": num_axioms,
                "completeness_score": completeness_score
            },
            "third_mind_insights": analysis["third_mind_insights"]
        }

        return json_ld

    def export_ontology_json(self, ontology_data: Dict[str, Any], filepath: str) -> None:
        """Exports secondary ontology to a JSON-LD formatted file."""
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(ontology_data, f, indent=2)
