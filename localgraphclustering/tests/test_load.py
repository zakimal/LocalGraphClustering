import localgraphclustering

def test_load():
    G = localgraphclustering.graph_class_local("localgraphclustering/tests/data/dolphins.edges",separator=" ")
    assert G.is_disconnected() == False