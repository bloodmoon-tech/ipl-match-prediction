from zipfile import ZipFile, ZIP_DEFLATED
from pathlib import Path

out_path = Path(r'c:\python data\ShivamBhardwaj_ProjectReport.docx')

content = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:w10="urn:schemas-microsoft-com:office:word" xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" xmlns:w15="http://schemas.microsoft.com/office/word/2012/wordml" xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup" xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk" xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml" xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape" mc:Ignorable="w14 w15 wp14">
  <w:body>
    <w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:t>Shivam Bhardwaj</w:t></w:r></w:p>
    <w:p><w:r><w:t>IPL Match Prediction Project Report</w:t></w:r></w:p>
    <w:p><w:r><w:t>IBM SkillsBuild Data Analytics with AI Academic Internship Program</w:t></w:r></w:p>
    <w:p><w:r><w:t>BharatCares in association with AICTE</w:t></w:r></w:p>
    <w:p/>
    <w:p><w:r><w:t>1. Introduction</w:t></w:r></w:p>
    <w:p><w:r><w:t>This project uses IPL match data from 2008 to 2026 to estimate whether the chasing team or the team batting first is more likely to win. It combines data preparation, machine learning, a FastAPI backend, and a Streamlit dashboard into a complete sports analytics application.</w:t></w:r></w:p>
    <w:p/>
    <w:p><w:r><w:t>2. Objectives</w:t></w:r></w:p>
    <w:p><w:r><w:t>- Analyze match data and important match variables</w:t></w:r></w:p>
    <w:p><w:r><w:t>- Identify the factors that influence the result of an IPL match</w:t></w:r></w:p>
    <w:p><w:r><w:t>- Build predictive models for classification</w:t></w:r></w:p>
    <w:p><w:r><w:t>- Compare multiple machine learning models and select the best one</w:t></w:r></w:p>
    <w:p/>
    <w:p><w:r><w:t>3. Dataset</w:t></w:r></w:p>
    <w:p><w:r><w:t>The project uses IPL match data covering multiple seasons. The dataset includes city, venue, teams, toss decision, target score, result, and match completion information. The file used was IPL_Matches_Data_2008_2026.csv and it is stored in the project data folder at data/IPL_Matches_Data_2008_2026.csv.</w:t></w:r></w:p>
    <w:p><w:r><w:t>Source: Kaggle</w:t></w:r></w:p>
    <w:p><w:r><w:t>Link: https://www.kaggle.com/code/shayanzk/ipl-2008-2026-what-19-seasons-of-data-actually-say</w:t></w:r></w:p>
    <w:p/>
    <w:p><w:r><w:t>4. Methodology</w:t></w:r></w:p>
    <w:p><w:r><w:t>The project starts with loading the dataset and cleaning the data. Completed matches involving the selected active teams are retained. Historical team names are standardized, batting-first and chasing-team variables are engineered, and categorical values are converted using OneHotEncoder.</w:t></w:r></w:p>
    <w:p><w:r><w:t>The prepared data is divided into training and testing sets. Logistic Regression, Random Forest, and XGBoost are compared using accuracy. The best pipeline is saved and reused by the application for future predictions.</w:t></w:r></w:p>
    <w:p/>
    <w:p><w:r><w:t>5. Technologies Used</w:t></w:r></w:p>
    <w:p><w:r><w:t>- Python</w:t></w:r></w:p>
    <w:p><w:r><w:t>- Pandas</w:t></w:r></w:p>
    <w:p><w:r><w:t>- NumPy</w:t></w:r></w:p>
    <w:p><w:r><w:t>- Matplotlib</w:t></w:r></w:p>
    <w:p><w:r><w:t>- Seaborn</w:t></w:r></w:p>
    <w:p><w:r><w:t>- Scikit-learn</w:t></w:r></w:p>
    <w:p><w:r><w:t>- XGBoost</w:t></w:r></w:p>
    <w:p><w:r><w:t>- Joblib</w:t></w:r></w:p>
    <w:p><w:r><w:t>- Streamlit for the frontend dashboard</w:t></w:r></w:p>
    <w:p><w:r><w:t>- FastAPI and Uvicorn for the prediction API</w:t></w:r></w:p>
    <w:p/>
    <w:p><w:r><w:t>6. Results</w:t></w:r></w:p>
    <w:p><w:r><w:t>The model comparison produced the following results on the held-out test split:</w:t></w:r></w:p>
    <w:p><w:r><w:t>- Logistic Regression Accuracy: 0.6701</w:t></w:r></w:p>
    <w:p><w:r><w:t>- Random Forest Accuracy: 0.6082</w:t></w:r></w:p>
    <w:p><w:r><w:t>- XGBoost Accuracy: 0.6701</w:t></w:r></w:p>
    <w:p><w:r><w:t>The best model was saved in the model folder as ipl_match_model.pkl for later use by the dashboard and API.</w:t></w:r></w:p>
    <w:p><w:r><w:t>The prepared dataset contains 966 completed matches. The historical chase-win rate is 54.45 percent and the average target is approximately 169 runs.</w:t></w:r></w:p>
    <w:p/>
    <w:p><w:r><w:t>7. Application Architecture</w:t></w:r></w:p>
    <w:p><w:r><w:t>The Streamlit frontend provides inputs for the two teams, city, toss winner, toss decision, and target score. It displays the predicted winner, confidence score, batting order, KPI cards, and historical infographic bars for match outcomes and city representation.</w:t></w:r></w:p>
    <w:p><w:r><w:t>The FastAPI backend exposes a POST /predict endpoint and interactive API documentation at /docs. Both services use the same reusable model functions in backend/model.py.</w:t></w:r></w:p>
    <w:p><w:r><w:t>To remain compatible with Windows systems where native DLLs may be restricted, XGBoost is optional and the dashboard uses lightweight HTML and CSS bars instead of PyArrow-backed chart helpers.</w:t></w:r></w:p>
    <w:p/>
    <w:p><w:r><w:t>8. Limitations and Future Scope</w:t></w:r></w:p>
    <w:p><w:r><w:t>The model learns from historical match conditions and is not a guaranteed forecast of future seasons. It does not currently use live player form, injuries, playing XI announcements, or live match feeds. Future improvements could include player-level statistics, current team form, real-time data ingestion, calibration, and additional seasons.</w:t></w:r></w:p>
    <w:p/>
    <w:p><w:r><w:t>9. Conclusion</w:t></w:r></w:p>
    <w:p><w:r><w:t>The IPL match prediction project demonstrates how data analytics and AI can be applied to sports forecasting through a complete, usable application. It combines a reproducible machine learning workflow with a clear dashboard and API, providing a strong foundation for future enhancements.</w:t></w:r></w:p>
    <w:p/>
    <w:p><w:r><w:t>10. Declaration</w:t></w:r></w:p>
    <w:p><w:r><w:t>This project was developed as part of the IBM SkillsBuild Data Analytics with AI Academic Internship Program in association with BharatCares and AICTE.</w:t></w:r></w:p>
    <w:sectPr>
      <w:pgSz w:w="12240" w:h="15840"/>
      <w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="720" w:footer="720" w:gutter="0"/>
    </w:sectPr>
  </w:body>
</w:document>
'''

content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>
'''

core = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>IPL Match Prediction Project Report</dc:title>
  <dc:creator>Shivam Bhardwaj</dc:creator>
  <cp:lastModifiedBy>Shivam Bhardwaj</cp:lastModifiedBy>
  <dcterms:created xsi:type="dcterms:W3CDTF">2026-09-21T00:00:00Z</dcterms:created>
  <dcterms:modified xsi:type="dcterms:W3CDTF">2026-09-21T00:00:00Z</dcterms:modified>
</cp:coreProperties>
'''

app = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>Microsoft Office Word</Application>
</Properties>
'''

rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>
'''

word_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
</Relationships>
'''

with ZipFile(out_path, 'w', ZIP_DEFLATED) as z:
    z.writestr('[Content_Types].xml', content_types)
    z.writestr('_rels/.rels', rels)
    z.writestr('docProps/core.xml', core)
    z.writestr('docProps/app.xml', app)
    z.writestr('word/document.xml', content)
    z.writestr('word/_rels/document.xml.rels', word_rels)

print(f'Created report: {out_path}')
print(f'Exists: {out_path.exists()}')
