class cliente{
    rut;
    nombre;
    edad;
    contrasena;

    setRut(rut){
        this.rut=rut;
    }
    setNombre(nom){ this.nombre=nom;}
    setEdad(ed){ this.edad=ed; }
    setContrasena(con){ this.contrasena=con; }
    getRut(){ return this.rut ;}
    getNombre(){ return this.nombre; }
    getEdad(){ return this.edad; }
    getContrasena(){return this.contrasena;}
    imprimir(){ return "Rut:"+this.rut+" Nombre:"+this.nombre+" Edad:"+this.edad+" Pass:"+this.contrasena;}

}