from asi_kedro.data_engineering.pipeline import create_pipeline 

class ProjectContext(KedroContext):
    project_name = "asi_kedro"
    
    def register_pipelines(self) -> Dict[str, Pipeline]:
        
        data_engineering_pipeline = create_pipeline()
        
        return {
            "__default__": data_engineering_pipeline,
            "de": data_engineering_pipeline
        }