"""
Secondary Ontology Completeness Extender.

Deconstructs primary ontologies (which contain implicit power dynamics / symbolic violence)
and extends them into critical, reflective secondary ontologies (RDF/JSON-LD knowledge graphs).
"""

import json
import re
from typing import Dict, List, Any, Set
from demo.gnosis import GnosisExtractor
from demo.cut_up_engine import CutUpEngine

class SecondaryOntologyExtender:
    def __init__(self):
        self.gnosis = GnosisExtractor()
        self.cut_up = CutUpEngine()

    def deconstruct_primary_ontology(self, primary_text: str, counter_text: str) -> Dict[str, Any]:
        """
        Collides primary text with counter-narrative text to surface hidden entities,
        redefine existing entities, and discover new subversive relationships.
        """
        recombined = self.cut_up.fold_in(primary_text, counter_text)
        analysis = self.gnosis.analyze_cut_up(recombined)

        primary_terms = self.gnosis.extract_keywords(primary_text, top_n=5)
        counter_terms = self.gnosis.extract_keywords(counter_text, top_n=5)

        # Entity Extraction
        entities = []
        for term, cnt in primary_terms:
            entities.append({
                "@id": f"ontology:Primary_{term.capitalize()}",
                "@type": "PrimaryEntity",
                "label": term,
                "status": "TargetOfDeconstruction",
                "critique": f"Embodiment of dominant control grammar in text."
            })

        for term, cnt in counter_terms:
            entities.append({
                "@id": f"ontology:Secondary_{term.capitalize()}",
                "@type": "SecondaryCriticalEntity",
                "label": term,
                "status": "LiberatoryCounterConcept",
                "role": f"Interferes with primary ontology repetition."
            })

        # Relationship Discovery via Juxtaposition Pairs
        relationships = []
        for w1, w2 in analysis["juxtaposition_pairs"]:
            relationships.append({
                "subject": f"ontology:{w1.capitalize()}",
                "predicate": "subverts_or_exposes",
                "object": f"ontology:{w2.capitalize()}",
                "context": f"Emergent relationship from fold-in juxtaposition."
            })

        # Axiom / Rule Formulations
        axioms = [
            "Axiom 1: Primary control ontologies naturalize their own authority through linear repetition.",
            "Axiom 2: Cut-up fold-in operations shatter implicit epistemic violence.",
            "Axiom 3: Liberatory secondary entities disrupt reproductive feedback loops."
        ]

        json_ld = {
            "@context": {
                "ontology": "http://burroughs.machine/schema/v1#",
                "PrimaryEntity": "ontology:PrimaryEntity",
                "SecondaryCriticalEntity": "ontology:SecondaryCriticalEntity",
                "subverts_or_exposes": "ontology:subverts_or_exposes"
            },
            "@graph": entities,
            "relationships": relationships,
            "axioms": axioms,
            "third_mind_insights": analysis["third_mind_insights"]
        }

        return json_ld

    def export_ontology_json(self, ontology_data: Dict[str, Any], filepath: str) -> None:
        """Exports secondary ontology to a JSON-LD formatted file."""
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(ontology_data, f, indent=2)
