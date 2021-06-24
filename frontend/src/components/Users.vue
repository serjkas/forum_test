<template>
    <div class="table-responsive">
    <table class="table table-striped table-sm">
        <thead>
        <tr>
            <th>ScriptName</th>
            <th>EffortsCount</th>
            <th>ConnectionsCount</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="report in reports" :key="report.id">
            <td>{{ report.scriptname}}</td>  
            <td>{{ report.effortscount}}</td>  
            <td>{{ report.connectionscount}}</td>  

        </tr>
        
        </tbody>
    </table>
    </div>

</template>