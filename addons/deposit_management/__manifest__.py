{
    'name':'Deposit Management System Tutorial',
    'version': '1.0',
    'author': 'ABK',
    'summary': "Here you can use banking system's deposit management system, "
               "like multiple banks handle, customers profile and its balance, "
               "transaction details and notification you can send also print "
               "transaction recepit.",
    'sequence': -111,
    'description':"Here you can use banking system's deposit management system, "
               "like multiple banks handle, customers profile and its balance, "
               "transaction details and notification you can send also print "
               "transaction recepit.",
    'category':'Banking',
    'website':'https://github.com/abk2035/',
    'depends':['base', 'contacts', 'mail'],
    'data':[
        "data/sequence_data.xml",
        "security/ir.model.access.csv",
        "security/group_view.xml",
        "views/bank_view.xml",
        "views/bank_transactions_view.xml",
        "views/customer_view.xml",
        "report/dm_bank_transaction_report.xml"
    ],
    'icon':'deposit_management/static/description/icon.png',
    'images': ['static/description/icon.png'],
    'application':True,
    'installable':True,

}