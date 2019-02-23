#include <iostream>
#include <string>
#include <stdio.h>

enum PersistenceType {
    File, Queue, Pathway
};

struct PersistenceAttribute {
    PersistenceType type;
    char value[30];
};

class DistrWorkPackage {
private:
    char _desc[200], _temp[200];
public:
    DistrWorkPackage(char *type) {
        sprintf(_desc, "Distributed work package for: %s", type);
    }

    void setFile(char *f, char *v) {
        sprintf(_temp, "\n File(%s): %s", f, v);
        strcat(_desc, _temp); // concat string: _desc = _desc + _temp
    }

    void setQueue(char *q, char *v) {
        sprintf(_temp, "\n Queue(%s): %s", q, v);
        strcat(_desc, _temp);
    }

    void setPathway(char *p, char *v)
    {
        sprintf(_temp, "\n  Pathway(%s): %s", p, v);
        strcat(_desc, _temp);
    }

    const char *getState() {
        return _desc;
    }
};

class Builder {
protected:
    DistrWorkPackage *_result;
public:
    virtual void configureFile(char*) = 0;
    virtual void configureQueue(char*) = 0;
    virtual void configurePathway(char*) = 0;
    DistrWorkPackage *getResult() {
        return _result;
    }
};

class UnixBuilder: public Builder {
public: 
    UnixBuilder() {
        _result = new DistrWorkPackage("Unix");
    }

    void configureFile(char *name) {
        _result->setFile("flatFile", name);
    }

    void configureQueue(char *queue) {
        _result->setQueue("FIFO", queue);
    }

    void configurePathway(char *type) {
        _result->setPathway("thread", type);
    }
};

class VmsBuilder: public Builder {
public:
    VmsBuilder() {
        _result = new DistrWorkPackage("Vms");
    }

    void configureFile(char *name) {
        _result->setFile("ISAM", name);
    }

    void configureQueue(char *queue) {
        _result->setQueue("priority", queue);
    }

    void configurePathway(char *type) {
        _result->setPathway("LWP", type);
    }
};

class Reader {
private: 
    Builder *_builder;
public:
    void setBuilder(Builder *b) {
        _builder = b;
    }

    void construct(PersistenceAttribute[], int);
};

void Reader::construct(PersistenceAttribute list[], int num) {
    for (int i = 0; i < num; i++) {
        if (list[i].type == File) {
            _builder->configureFile(list[i].value);
        }
        else if (list[i].type == Queue) {
            _builder->configureQueue(list[i].value);
        }
        else if (list[i].type == Pathway) {
            _builder->configurePathway(list[i].value);
        }
    }
}

const int NUM_ENTRIES = 6;
PersistenceAttribute input[NUM_ENTRIES] = {
    {File, "state.dat"},
    {File, "config.sys"},
    {Queue, "compute"},
    {Queue, "log"},
    {Pathway, "authentication"},
    {Pathway, "error processing"}
};

int main() {
    UnixBuilder unixBuilder;
    VmsBuilder vmsBuilder;
    Reader reader;

    reader.setBuilder(&unixBuilder);
    reader.construct(input, NUM_ENTRIES);
    std::cout << unixBuilder.getResult()->getState() << std::endl;

    reader.setBuilder(&vmsBuilder);
    reader.construct(input, NUM_ENTRIES);
    std::cout << vmsBuilder.getResult()->getState() << std::endl;
    return 0;
}

/*
output:
Distributed Work Package for: Unix
  File(flatFile): state.dat
  File(flatFile): config.sys
  Queue(FIFO): compute
  Queue(FIFO): log
  Pathway(thread): authentication
  Pathway(thread): error processing
Distributed Work Package for: Vms
  File(ISAM): state.dat
  File(ISAM): config.sys
  Queue(priority): compute
  Queue(priority): log
  Pathway(LWP): authentication
  Pathway(LWP): error processing
*/