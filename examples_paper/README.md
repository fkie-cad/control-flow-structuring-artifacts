# Examples from the Paper

In the Paper, we only presented the outputs of *some* of the decompilers considered in the paper and evaluation.
In order to be able to compare all decompiler outputs, we provide all decompiler outputs as C-files containing the actual, not normalized, output for all considered examples.

The decompiler outputs of `test_1`, `test_3`, and `test_4` in the paper originate from the binary `example_samples` and were compiled without any optimization. 
The corresponding decompiler-outputs are provided in the C-files without the `O3` ending.

The decompiler output of `test_2` in the paper originates from the binary `example_samples_O3` and was decompiled with optimization level 3. 
The corresponding decompiler-outputs are provided in the C-files with the ending `O3`.


#### Remarks to SAILR

The examples in the paper were decompiled with the SAILR implementation mentioned in the corresponding paper, i.e., we used `angr 9.2.100` and the implementation from the sail-eval Repository (https://github.com/mahaloz/sailr-eval) at commit `f5a30c3a0312a669e9f6f87acab7473618dd97cf`.
These decompiler outputs are saved in `sailr.c` and `sailr_O3.c`.

Since SAILR is now also integrated into angr, and we used this integrated version for our evaluation, we also present the output of SAILR in `angr 9.2.146`. 
These decompiler outputs are saved in `sailr_angr.c` and `sailr_angr_O3.c`


#### Remarks to DREAM

Because the original DREAM implementation does not work with recent IDA Pro versions anymore, we opted to use a different implementation.

Fortunately, the authors of the SAILR Paper reimplemented parts of the DREAM algorithm and integrated it into angr. 
However, we noticed that the implementation seems not to be 100% accurate. 
For example, the DREAM approach would group the if-conditions before `Block 2` and `Block 3` of `test_2` in `dream_angr.c` into an if-else construct. 
Due to its stability, we still decided to use this implementation for the overall evaluation.

However, for some of the examples in the paper and the direct comparison, we wanted an output that is more closely to the actual DREAM approach. 
Since dewolf is only an extension of DREAM, we tried to modify their implementation to match the DREAM approach more closely. 
These outputs are present in `dream_dewolf.c` and `dream_dwolf_O3.c`. 
Nevertheless, we also provide the dream output resulting from the implementation integrated intro angr in `dream_angr.c` and `dream_angr_O3.c`.

**Modifications:**

For reproducibility, these are the modifications we applied to dewolf (commit `b42aa6816c13467a597471bdd54b943ea7511723`) to achive the DREAM results:

File `decompiler/pipeline/controlflowanalysis/restructuring_commons/acyclic_restructuring.py`
```diff
@@ -39,7 +38,7 @@ class AcyclicRegionRestructurer:

def restructure(self):
"""Restructure the acyclic transition graph."""
-        acyclic_region_finder: AcyclicRegionFinder = AcyclicRegionFinderFactory.create(Strategy.improved_dream)(self.t_cfg)
+        acyclic_region_finder: AcyclicRegionFinder = AcyclicRegionFinderFactory.create(Strategy.dream)(self.t_cfg)
while len(self.t_cfg) > 1:
```

File `decompiler/pipeline/controlflowanalysis/restructuring_commons/condition_aware_refinement.py`
```diff
@@ -32,8 +32,8 @@ class ConditionAwareRefinement(BaseClassConditionAwareRefinement):

REFINEMENT_PIPELINE = [
    InitialSwitchNodeConstructor.construct,
-        MissingCaseFinderCondition.find,
-        SwitchExtractor.extract,
+        # MissingCaseFinderCondition.find,
+        # SwitchExtractor.extract,
MissingCaseFinderSequence.find,
]
```

File `decompiler/pipeline/controlflowanalysis/restructuring_commons/condition_aware_refinement_commons/initial_switch_node_constructer.py`
```diff
@@ -217,8 +217,8 @@ class InitialSwitchNodeConstructor(BaseClassConditionAwareRefinement):
def construct(cls, asforest: AbstractSyntaxForest, options: RestructuringOptions) -> Set[SwitchNode]:
"""Constructs initial switch nodes if possible."""
initial_switch_constructor = cls(asforest, options)
-        for cond_node in asforest.get_condition_nodes_post_order(asforest.current_root):
-            initial_switch_constructor._extract_case_nodes_from_nested_condition(cond_node)
+        # for cond_node in asforest.get_condition_nodes_post_order(asforest.current_root):
+        #     initial_switch_constructor._extract_case_nodes_from_nested_condition(cond_node)
for seq_node in asforest.get_sequence_nodes_post_order(asforest.current_root):
```

File `decompiler/pipeline/controlflowanalysis/restructuring_commons/condition_aware_refinement_commons/missing_case_finder_sequence.py`
```diff
@@ -52,7 +52,7 @@ class MissingCaseFinderSequence(MissingCaseFinder):
             if not missing_case_finder._switch_node_of_expression:
                 continue
 
-            missing_case_finder._add_missing_cases()
+            # missing_case_finder._add_missing_cases()
             if seq_node in asforest:
                 missing_case_finder._add_default_case()

```
