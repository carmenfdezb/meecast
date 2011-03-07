#ifndef MAINPAGE_H
#define MAINPAGE_H

#include <MApplicationPage>
#include <MLabel>
#include <MComboBox>
#include <MButton>
#include <QGraphicsLinearLayout>
#include <MSceneManager>
#include "core.h"

#include "stationpage.h"

class MainPage : public MApplicationPage
{
    Q_OBJECT
public:
    MainPage(QGraphicsItem *parent = 0);
    virtual ~MainPage();

protected:
    virtual void createContent();

private slots:
    void addClicked();

};

#endif // MAINPAGE_H
