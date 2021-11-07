import { useState, useEffect } from "react";
import axios from "axios";

const documents_url = "http://127.0.0.1:8000/api/documents/";

type DocArrType = {
  id: number;
  title: string;
  pdf_doc: string;
}[];

const Documents = () => {
  const [documents, setDocuments] = useState<DocArrType>([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const { data } = await axios.get(documents_url);
      setDocuments(data);
    } catch (error) {
      throw error;
    }
  };

  return (
    <div>
      <p>document list component</p>
      {documents.map((item, index) => {
        return (
          <div key={index}>
            <div>{item.title}</div>
            <div>{item.pdf_doc}</div>
          </div>
        );
      })}
    </div>
  );
};

export default Documents;
