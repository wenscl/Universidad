using Microsoft.Owin;
using Owin;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

[assembly: OwinStartup(typeof(JuegoCromix.Web.Startup))]
namespace JuegoCromix.Web
{
    public class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            // Any connection or hub wire up any configuration should go here
            app.MapSignalR();
        }
    }
}