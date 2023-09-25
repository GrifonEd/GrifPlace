package com.example.grifplace;

public class ModelPdf {

    String id,type,area,password;

    public ModelPdf() {
    }

    public ModelPdf(String id, String type, String area , String password){

        this.id = id;
        this.type = type;
        this.area = area;
        this.password = password;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getArea() {
        return area;
    }

    public void setArea(String area) {
        this.area = area;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
}
