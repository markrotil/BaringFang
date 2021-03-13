function buildplot_entertainment() {
    d3.json("/entertainment").then(function (data) {
        var ticker = data.entertainment_stocks[0].Ticker;
        var adj_Close = data.entertainment_stocks[0].Adj_Close;
        var date = data.entertainment_stocks[0].Date
        var ticker1 = data.entertainment_stocks[1].Ticker;
        var adj_Close1 = data.entertainment_stocks[1].Adj_Close;
        var date1 = data.entertainment_stocks[1].Date
        var ticker2 = data.entertainment_stocks[2].Ticker;
        var adj_Close2 = data.entertainment_stocks[2].Adj_Close;
        var date2 = data.entertainment_stocks[2].Date;
    })
}
